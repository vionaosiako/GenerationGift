from rest_framework import serializers
from . models import Employer


class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Employer
        fields = ['job_title','date_posted','description', 'category', 'location' , 'approximate_salary' , 'deadline','user']
        
    
