from rest_framework import serializers
from .models import ProjectPitch


class ProjectPitchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectPitch
        fields = ['id', 'title', 'description', 'total_cost', 'mpesa_no']