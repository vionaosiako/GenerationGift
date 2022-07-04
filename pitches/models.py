from django.db import models


class ProjectPitch(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    total_cost = models.IntegerField()
    mpesa_no = models.IntegerField()
    
    def __str__(self):
        return self.title 
    
    
    
    
    
