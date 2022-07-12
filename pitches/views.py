from .serializers import ProjectPitchSerializer
from rest_framework import viewsets
from .models import ProjectPitch

class ProjectPitchViewset(viewsets.ModelViewSet):
    serializer_class = ProjectPitchSerializer
    queryset = ProjectPitch.objects.all()
