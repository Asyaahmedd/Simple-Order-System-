import re
import pytest
from products import views
from products.models import Product

@pytest.fixture
def product(name,describtion,owner,price,quantity):
    return Product.objects.create(
        name= "calender",
        describtion='This is a calender',
        owner='sara',
        price=1.77,
        quantity=1
    )

