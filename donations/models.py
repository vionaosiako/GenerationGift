from django.db import models

# Create your models here.

class Donations(models.Model):
    items = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    time = models.TimeField(null=True)
    donation_date = models.DateTimeField(null=True, blank=True)
    venue = models.TextField(max_length=30, null=True)


    def __str__(self):
        return self.name

    def save_donations(self):
        self.save()

    def delete_donations(self):
        self.delete()

    def update_donations(self):
        self.update()
