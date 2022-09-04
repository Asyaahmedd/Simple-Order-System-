from django.db import models
from django.contrib.auth.models import User
import datetime
class Product(models.Model):
    name = models.CharField(max_length=200)
    describtion= models.TextField()
    owner = models.ForeignKey('auth.User',default=1,related_name='products',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']

class Purchase(models.Model):
    product = models.ForeignKey(Product, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)

    class Meta:
        ordering=['price']
    

    
    



