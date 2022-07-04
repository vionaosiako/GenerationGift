from django.db import models

# Create your models here.
class Employer(models.Model):
    job_title= models.CharField(max_length=100)
    date_posted= models.DateField(auto_now_add=True)
    description = models.TextField()
    category = models.CharField(max_length=40, blank=True,null=True )
    location = models.CharField(max_length=100)
    approximate_sallary = models.PositiveIntegerField(default=0)
    deadline = models.DateTimeField(auto_now=True)
    
    
    def create_job(self):
        self.save()
        
    def delete_job(self):
        self.delete()
        
        
    def update_job(self):
        self.update()
        
   
        
    
    
    
    