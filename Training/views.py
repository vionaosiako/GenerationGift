from .serializers import TrainingSerializer
from rest_framework import viewsets
from .models import Training
# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import MultiPartParser

# from drf_yasg.utils import swagger_auto_schema
# Create your views here.

# @swagger_auto_schema(request_body=TrainingSerializer)
class TrainingViewset(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    
    # def createTraining(self, request, filename, format=None):
    #     # file_obj = request.data['file']
    #     # ...
    #     # do some stuff with uploaded file
    #     print_r(request)
    #     print_r(filename)
    #     return Response(status=204)
