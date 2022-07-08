from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
    job_title= models.CharField(max_length=100)
    description = models.TextField()
    date_posted= models.DateField(auto_now_add=True)
    category = models.CharField(max_length=40, blank=True,null=True )
    location = models.CharField(max_length=100)
    approximate_salary = models.PositiveIntegerField(default=0)
    deadline = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employer',blank=True, null=True)
    
    def create_job(self):
        self.save()
        
    def delete_job(self):
        self.delete()
        
        
    def update_job(self):
        self.update()
