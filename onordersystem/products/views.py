from urllib import response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from products.models import Product,Purchase
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from products.permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializers,PurchaseSerializers,UserSerializers
from rest_framework import permissions

# Create your views(endpoint) here.
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_products(request):
    if request.method== 'GET':
        #get all products
        products = Product.objects.all()
        # serialize them
        serializer = ProductSerializers(products,many=True)
        #return json
        return JsonResponse({'products':serializer.data})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    if request.method =='POST':
        serializer= ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def modify_product(request,id):
    try :
        product=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer = ProductSerializers(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request,id):
    try :
        product=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsOwnerOrReadOnly])
@permission_classes([IsAuthenticated])
def get_purchased(request,id):
    try :
        purchases=Purchase.objects.filter(user=request.user)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method== 'GET':
        # serialize them
        serializer = PurchaseSerializers(purchases,many=True)
        #return json
        return JsonResponse({'purchases':serializer.data})

@api_view(['POST'])
@permission_classes([IsOwnerOrReadOnly])
@permission_classes([IsAuthenticated])
def purchase_product(request):
    if request.method =='POST':
        serializer= PurchaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET'])
def user_list_products(request):
    #list all purshased products for each user 
    if request.method== 'GET': 
        queryset  = User.objects.all()
        serializer = UserSerializers(queryset ,many=True)
        return JsonResponse({'products':serializer.data})










