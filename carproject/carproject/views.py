from django.shortcuts import render
from carbrand.models import Carbrand 
from carmodel.models import CarModel 

def home(request , carbrnad_slug =None):
    data = CarModel.objects.all()
    form = Carbrand.objects.all()
    if carbrnad_slug is not None:
        brand =Carbrand.objects.get(slug = carbrnad_slug)
        data = CarModel.objects.filter(brand=brand)
    return render(request,'home.html' ,{"data":data ,"brands":form })