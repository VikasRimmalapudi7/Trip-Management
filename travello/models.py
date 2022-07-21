from django.db import models

# Create your models here.
class Destination(models.Model):


    
    desc=models.TextField(max_length=200)
    price= models.IntegerField()
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)