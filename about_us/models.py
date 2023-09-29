from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
import random
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       birthday = models.DateField(null=True, blank=True)
       occupation = models.CharField(max_length=100, null=True, blank=True)
       height = models.FloatField(null=True, blank=True)
       weight = models.FloatField(null=True, blank=True)
       age = models.IntegerField(null=True, blank=True)
# class CustomUser(AbstractUser):
#     is_approved = models.BooleanField(default=False)

# ALL CLASSES
class Profpic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return f'{self.user.username} Profile' 

class JerseyNumPic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return f'{self.user.username} Jersey Number' 

class Birthday(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.birthday}'

class Occupation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.occupation}'

class Year_Joined(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_joined = models.DateField()

    def __str__(self):
        return f'{self.year_joined}'

class Height(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.height}'

class Weight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.weight}'

class Age(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.age}'

class TinNum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tin = models.IntegerField()

    def __str__(self):
        return f'{self.tin}'

class JerseyNum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jerseynum = models.IntegerField()

    def __str__(self):
        return f'{self.jerseynum}'

class GcashNum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gcashnum = models.IntegerField()

    def __str__(self):
        return f'{self.gcashnum}'

class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.team}'

# END CLASS

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

def generate_random_id():
    return random.randint(10000, 99999)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birthday = models.DateField()
#     contact_no = models.CharField(max_length=20)
#     profile_picture = models.ImageField(upload_to='media/images/')
#     occupation = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)

#     def __str__(self):
#         return self.user.username


class Announcements(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  
    picture = models.ImageField(upload_to='media/images/') 
    date_created = models.DateTimeField(auto_now_add=True)


# class PBAdmin(models.Model):
#     name = models.CharField(max_length=500)
#     password = models.CharField(max_length=50)

