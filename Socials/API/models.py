
# Create your models here.
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    

class InstagramUser(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=255)
    biography = models.TextField()
    followers_count = models.IntegerField()
    follows_count = models.IntegerField()
    is_private = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    profile_pic_url_hd = models.URLField()
    posts_count = models.IntegerField()
    highlight_reel_count = models.IntegerField()
    igtv_video_count = models.IntegerField()
    about_this_account_country = models.CharField(max_length=255)
    date_joined = models.DateField()

    def _str_(self):
        return self.full_name
