from django.urls import path
from .views import add_to_cart,cart_home,cart_delete,update_cart # importing views from current directory (.import)
urlpatterns=[
    path('add_to_cart/<int:id>', add_to_cart,name='add_to_cart'),
    path('cartpage',cart_home,name='cartpage'),
    path('cart_delete/<int:id>/',cart_delete,name='cart_delete'),
    path('updatecart/<int:id>/',update_cart,name='updatecart'),
]  