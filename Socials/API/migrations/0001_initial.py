# Generated by Django 5.0.3 on 2024-03-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramUser',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('followers_count', models.IntegerField()),
                ('follows_count', models.IntegerField()),
                ('is_private', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('profile_pic_url_hd', models.URLField()),
                ('posts_count', models.IntegerField()),
                ('highlight_reel_count', models.IntegerField()),
                ('igtv_video_count', models.IntegerField()),
                ('about_this_account_country', models.CharField(max_length=255)),
                ('date_joined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
