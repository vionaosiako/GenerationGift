from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField()
    bio= models.TextField(max_length=355,default='my bio',blank=True)
    name = models.CharField(max_length=65,blank=True)
    email = models.EmailField(max_length=120,blank=True)
    location = models.CharField(max_length=65,blank=True)
    contact = models.CharField(max_length=65,blank=True)
    
    def __str__(self):
            return f'{self.user.username} Profile'

    
    def create_user_profile(sender, instance, created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    def save_user_profile(sender, instance,**kwargs):
        instance.profile.save()