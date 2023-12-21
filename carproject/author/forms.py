
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']
        
class Userchangeform(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']