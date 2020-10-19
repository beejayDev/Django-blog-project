from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .models import Profile

class CreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """ 
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']


class AuthForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Email or password")

class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
