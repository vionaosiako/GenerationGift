from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donations(models.Model):
    items = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    time = models.TimeField(null=True)
    donation_date = models.DateTimeField(null=True, blank=True)
    venue = models.TextField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation',blank=True, null=True)


    def __str__(self):
        return self.name

    def save_donations(self):
        self.save()

    def delete_donations(self):
        self.delete()

    def update_donations(self):
        self.update()
