from django.urls import path
from products import views

urlpatterns = [
    path('products/',views.get_products),
    path('products/create/',views.create_product),
    path('products/modify/<int:id>',views.modify_product),
    path('products/delete/<int:id>',views.delete_product),
    path('purchases/<int:id>',views.get_purchased),
    path('purchases/create/',views.purchase_product),
    path('users/',views.user_list_products),

]