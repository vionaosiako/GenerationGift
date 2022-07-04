from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images')
    bio= models.TextField(max_length=355,default='my bio',blank=True)
    name = models.CharField(max_length=65,blank=True)
    email = models.EmailField(max_length=120,blank=True)
    location = models.CharField(max_length=65,blank=True)
    contact = models.CharField(max_length=65,blank=True)
    
    

    
    
    def __str__(self):
        
        return self.user.username

    
    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance,**kwargs):
        instance.profile.save()
    