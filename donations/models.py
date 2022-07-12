from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Donations(models.Model):
    poster=CloudinaryField('image',null=True,blank=True)
    items = models.CharField(max_length=30)
    donorname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    donationdate = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation',blank=True, null=True)


    # def __str__(self):
    #     return self.donorname

    def save_donations(self):
        self.save()

    def delete_donations(self):
        self.delete()

    def update_donations(self):
        self.update()
