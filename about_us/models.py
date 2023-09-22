from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image

# class CustomUser(AbstractUser):
#     is_approved = models.BooleanField(default=False)

class ParishianClub(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.name

class ClubMembers(models.Model):
    name = models.CharField(max_length=500)
    year_joined = models.IntegerField()
    # pfp = models.ImageField(upload_to='media/images')

class Announcements(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  
    picture = models.ImageField(upload_to='media/images/') 
    date_created = models.DateTimeField(auto_now_add=True)


# class PBAdmin(models.Model):
#     name = models.CharField(max_length=500)
#     password = models.CharField(max_length=50)

