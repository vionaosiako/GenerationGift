# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import ProjectPitch
# from .serializers import PitchSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from pitches import serializers
from .serializers import ProjectPitchSerializer
from rest_framework import viewsets
from .models import ProjectPitch

class ProjectPitchViewset(viewsets.ModelViewSet):
    serializer_class = ProjectPitchSerializer
    queryset = ProjectPitch.objects.all()

# @api_view(['GET', 'POST'])
# def pitch_list(request):
    
#     if request.method == 'GET':
#         pitches = ProjectPitch.objects.all()
#         serializer = PitchSerializer(pitches, many=True)
#         return Response(serializer.data)
#         # return JsonResponse({'pitches':serializer.data})
    
#     if request.method == 'POST':
#         serializer = PitchSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
# @api_view(['GET', 'PUT', 'DELETE'])   
# def pitch_detail(request, id):
    
#     try:
#         pitch = ProjectPitch.objects.get(pk=id)
#     except ProjectPitch.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PitchSerializer(pitch)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = PitchSerializer(pitch, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         pitch.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
