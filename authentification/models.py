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