from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Training(models.Model):
    title=models.CharField(max_length=200)
    poster=CloudinaryField('image')
    description=models.TextField()
    venue=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    eventdate=models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    @classmethod
    def search_by_title(cls,search_term):
        title = cls.objects.filter(title__icontains=search_term).all()
        return title
