from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .serializers import ProfileSerializer
from .models import Profile
from .forms import RegistrationForm,CustomAuthForm
from django.urls import reverse_lazy

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CustomLoginView():  #created custom loginView in order to use a different form class
    template_name = 'instagram/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse_lazy('home')

def get_profile_url(self):
    Profile.objects.format.json()
    return render('api.html')

    