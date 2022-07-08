from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Training(models.Model):
    title=models.CharField(max_length=200)
    poster=CloudinaryField('image',null=True,blank=True)
    description=models.TextField()
    venue=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    eventdate=models.DateField(null=True,blank=True)
    eventtime=models.TimeField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training',blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def search_by_title(cls,search_term):
        title = cls.objects.filter(title__icontains=search_term).all()
        return title