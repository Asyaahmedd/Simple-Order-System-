import pytest
from rest_framework.test import APIClient
from products.models import Product
client = APIClient()
@pytest.mark.django_db
def test_create_product():
    payload = dict(
        name= "calender",
        describtion='This is a calender',
        owner='sara',
        price=1.7,
        quantity=1 )
    response = client.post('/products/create/',payload)
    return response
#This is not working
""""@pytest.mark.django_db
def test_get_products():
    client = APIClient()
    response = client.get(path='/products/', format='json')
    assert response.status_code == 200"""


