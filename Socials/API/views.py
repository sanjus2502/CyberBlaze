from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UsernameForm 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required



from .forms import UsernameForm
from .models import InstagramUser
from datetime import datetime
import requests
from apify_client import ApifyClient

def fetch_instagram_data(username):
  
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
           
        }
        filtered_data.append(filtered_item)

    if not filtered_data:
        print("Failed to retrieve data from Apify.")
        return None

    instagram_user_data = filtered_data[0]
    return instagram_user_data

def fetch_instagram(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        if username:
            instagram_user_data = fetch_instagram_data(username)
            if instagram_user_data:
               
                context = {'instagram_user': instagram_user_data}
            
                return render(request, 'index.html', context)
            else:
                return JsonResponse({'error': 'Failed to fetch Instagram data.'}, status=400)
        else:
            return JsonResponse({'error': 'Username not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


def fetch_instagram(request):
    form = None  
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            instagram_user = fetch_instagram_data(username)
            if instagram_user:
                return render(request, 'index.html', {'instagram_user': instagram_user})
    else:
        form = UsernameForm()

    return render(request, 'index.html', {'form': form})

