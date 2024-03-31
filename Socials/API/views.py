from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UsernameForm  # Import your UsernameForm if not already imported




from .forms import UsernameForm
from .models import InstagramUser
from datetime import datetime
import requests
from apify_client import ApifyClient

def fetch_instagram_data(username):
    # Your implementation here
    pass

def homepage(request):
    return render(request,"index.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)  

       if user is not None:
          auth.login(request, user)
          return redirect('/')
       else:
          messages.info(request, 'Credentials Invalid')
          return redirect('login')
    else:
      return render(request,"login.html")

def register(request):
 if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    if User.objects.filter(email=email).exists():
       messages.info(request, 'Email Already Used')
       return redirect('register')
    
    elif User.objects.filter(username=username).exists():
       messages.info(request, 'Username Already Used')
       return redirect('register')
    
    else:
       user = User.objects.create_user(username=username,email=email, password=password)
       user.save();
    return redirect('login')
 else:
    return render(request,"register.html")
 




APIFY_TOKEN = "apify_api_1ARMClTZxP9VYafbeEJyhoBMlj1DMY104rvI"
RAPIDAPI_KEY = "e7f93e7eecmshb025767d39d0611p10a1d3jsnc1cdb354d681"

def fetch_instagram_data(username):
    client = ApifyClient(APIFY_TOKEN)
    run_input = {"usernames": [username]}
    run = client.actor("dSCLg0C3YEZ83HzYX").call(run_input=run_input)

    filtered_data = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        filtered_item = {
            "id": item.get("id"),
            "fullName": item.get("fullName"),
            "biography": item.get("biography"),
            "followersCount": item.get("followersCount"),
            "followsCount": item.get("followsCount"),
            "private": item.get("private"),
            "verified": item.get("verified"),
            "profilePicUrlHD": item.get("profilePicUrlHD"),
            "postsCount": item.get("postsCount"),
            "highlightReelCount": item.get("highlightReelCount"),
            "igtvVideoCount": item.get("igtvVideoCount"),
        }
        filtered_data.append(filtered_item)
    print(filtered_item)
    if not filtered_data:
        print("Failed to retrieve data from Apify.")
        return None

    user_id = filtered_data[0]["id"]  


    url = f"https://instagram-api-20231.p.rapidapi.com/api/get_user_country/{user_id}"
    headers = {
        "X-RapidAPI-Key": "e7f93e7eecmshb025767d39d0611p10a1d3jsnc1cdb354d681",
        "X-RapidAPI-Host": "instagram-api-20231.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        data = response.json()["data"]
        about_country = data.get("about_this_account_country")
        date_joined = data.get("date_joined")

        combined_data = {
            "instagram_data": filtered_data,
            "about_this_account_country": about_country,
            "date_joined": date_joined
        }

        instagram_user_data = combined_data['instagram_data'][0]
        instagram_user, created = InstagramUser.objects.get_or_create(
            id=instagram_user_data['id'],
            defaults={
                'full_name': instagram_user_data['fullName'],
                'biography': instagram_user_data['biography'],
                'followers_count': instagram_user_data['followersCount'],
                'follows_count': instagram_user_data['followsCount'],
                'is_private': instagram_user_data['private'],
                'is_verified': instagram_user_data['verified'],
                'profile_pic_url_hd': instagram_user_data['profilePicUrlHD'],
                'posts_count': instagram_user_data['postsCount'],
                'highlight_reel_count': instagram_user_data['highlightReelCount'],
                'igtv_video_count': instagram_user_data['igtvVideoCount'],
                'about_this_account_country': combined_data['about_this_account_country'],
                'date_joined': datetime.strptime(combined_data['date_joined'], '%B %Y')
            }
        )

        if created:
            return instagram_user
        else:
            return None
    else:
        print("Failed to retrieve data from RapidAPI. Status code:", response.status_code)
        return None

def fetch_instagram(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            instagram_user = fetch_instagram_data(username)
            if instagram_user:
                return render(request, 'index.html', {'instagram_user': instagram_user})
                # return JsonResponse({'instagram_user': instagram_user})
    else:
        form = UsernameForm()

    return render(request, 'index.html', {'form': form})

    # return JsonResponse({'form': form.errors}, status=400)




from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    # Get CSRF token
    csrf_token = get_token(request)
    
    # Return CSRF token in JSON response
    return JsonResponse({'csrfToken': csrf_token})





def fetch_instagram(request):
    instagram_user = None  # Default value if the user is not found

    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            instagram_user = fetch_instagram_data(username)  # Fetch Instagram user data
    else:
        form = UsernameForm()

    return render(request, 'index.html', {'form': form, 'instagram_user': instagram_user})