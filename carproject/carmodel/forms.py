
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . models import CarModel ,CommentModel

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ('author',)
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name' ,'email' ,'body']
        
class RegistrationForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
        model = User
        fields =['username','first_name','last_name','email']
class Userchangeform(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']