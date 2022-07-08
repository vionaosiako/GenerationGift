from django.db import models
from django.contrib.auth.models import User


class ProjectPitch(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    total_cost = models.IntegerField()
    mpesa_no = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainings',blank=True, null=True)
    
    def __str__(self):
        return self.title 
