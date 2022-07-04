from .serializers import TrainingSerializer
from rest_framework import viewsets
from .models import Training

# Create your views here.

class TrainingViewset(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
