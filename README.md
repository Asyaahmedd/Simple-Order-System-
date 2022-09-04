# Simple Order System using Django and Django Rest Framework 
Online ordering system in which administrator users can add products and users can purchase this product.

## Administrator User:

  System user, they can access and use all the available APIs. They can create, modify, and delete Products. They are NOT allowed to purchase their products.
  
## Normal User:

   This is a user that has a list of products that they can purchase. They can list their purchased products.
   
## APIs Required:

  • create_product	allows admin users to create a product.
  
  • modify_product	allows admin user to modify a product that already exists.
  
  • delete_product	allows admin user to delete a product that already exists.
  
  • get_products		allows admin users to retrieve a list of all products that exist.
  
  • purchase_product	allows normal users to purchase a product.
  
  • get_purchased	allows normal user to retrieve a list of their products

