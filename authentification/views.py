from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .serializers import ProfileSerializer,UserSerializer
from .models import Profile
from .forms import RegistrationForm,CustomAuthForm,UpdateUserProfileForm,UpdateUserForm
from django.urls import reverse_lazy

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomLoginView():  #created custom loginView in order to use a different form class
    template_name = ''
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse_lazy('home')
    
        model = get_user_model()
        fields = ('id', 'username')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    serializer_class = UserSerializer
    
    def get_object(self):
        self.request.user









def profile(request, username):
    return render(request)


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, params)

@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid() and prof_form.is_valid():
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, params)

    