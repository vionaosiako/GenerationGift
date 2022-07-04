from .models import Training
from rest_framework import serializers

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Training
        fields = ['id','title','poster','description','venue','category','eventdate']