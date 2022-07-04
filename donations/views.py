from .serializers import DonationsSerializer
from rest_framework import viewsets
from .models import Donations

# Create your views here.

class DonationsViewset(viewsets.ModelViewSet):
    serializer_class = DonationsSerializer
    queryset = Donations.objects.all()




































# from django.shortcuts import render, redirect

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .serializers import DonationsSerializer

# from .models import Donations

# Create your views here.

# class DonationsView(APIView):
#      #base class for our API view function.
#     def get(self, request, format=None):

#         #define a get method 
#         all_donations = Donations.objects.all()

#         #serialize the Django model objects 
#         serializers = DonationsSerializer(all_donations, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
        
#         serializers = DonationsSerializer(data=request.data)

#         # serialize the data in the request
#         if serializers.is_valid():

            
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,) 



