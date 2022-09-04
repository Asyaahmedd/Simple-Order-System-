from pyexpat import model
from rest_framework import serializers
from .models import Product, Purchase
from django.contrib.auth.models import User

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ('__all__')

class UserSerializers(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many = True,queryset=Product.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['products','owner']

        
class PurchaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('__all__')
