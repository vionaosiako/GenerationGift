

from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms
from .models import Profile


class CustomAuthForm():

    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'username'})
        self.fields['password'].widget.attrs.update({'placeholder':'password'})
        

    

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'email'})
        self.fields['username'].widget.attrs.update({'placeholder':'username'})
        self.fields['password1'].widget.attrs.update({'placeholder':'password'})
    
        self.fields['password2'].widget.attrs.update({'placeholder':'confirm password'})
        
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio', 'contact']
