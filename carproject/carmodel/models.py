from django.db import models
from carbrand.models import Carbrand 
from carbrand.models import Carbrand 
from django.contrib.auth.models import User
# Create your models here.
class CarModel(models.Model):
    car_name = models.CharField(max_length=50 )
    price = models.CharField(max_length=20)
    image_field =models.ImageField(upload_to='carmodel/media/uploads/' ,blank=True ,null=True)
    description = models.TextField(blank=True , null = True)
    quantity = models.PositiveIntegerField(blank =True,null = True)
    brand = models.ForeignKey(Carbrand ,on_delete =models.CASCADE)
    author = models.ForeignKey(User ,on_delete =models.CASCADE)
    def __str__(self) :
        return self.car_name
    
class CommentModel(models.Model):
    Carmodel = models.ForeignKey(CarModel ,on_delete= models.CASCADE , related_name ='comments')
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    body = models.TextField(blank=True, null =True)
    created_time = models.DateTimeField(auto_now_add = True)