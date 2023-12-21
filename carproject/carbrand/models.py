from django.db import models

# Create your models here.
class Carbrand(models.Model):
    name = models.CharField(max_length=50 )
    slug = models.SlugField(max_length =100 , unique =True , blank=True ,null =True)
    def __str__(self):
        return self.name