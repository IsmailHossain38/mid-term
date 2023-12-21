from . import forms 
from .models import Carbrand

class CarForm(forms.ModelForm):
    class Meta:
        model = Carbrand
        fields ='__all__'