from .serializers import TrainingSerializer
from rest_framework import viewsets
from .models import Training

from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(request_body=TrainingSerializer)
class TrainingViewset(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
