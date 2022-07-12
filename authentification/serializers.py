from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','name', 'profile_picture', 'bio', 'location', 'contact']
        
        
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    #password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    #password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','profile','url']
    def save(self, **kwargs):
        user = models.User(
        username=self.validated_data['username'],
        email=self.validated_data['email']
    )
        password = self.validated_data['password']
        #password2 = self.validated_data['password2']
        #if password != password2:
            #raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.save()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.name
        # ...
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer