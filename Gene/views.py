from .serializers import EmployerSerializer
from rest_framework import viewsets
from .models import Employer

class EmployerViewset(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()