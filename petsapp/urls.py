from django.urls import path
from .import views # importing views from current directory (.import)
urlpatterns=[
    path('pets-list/',views.pets_list,name='pets-list'),
    path('cat-list/',views.cat_list,name='cat-list'), # register url of cat_list
    path('dog-list/',views.dog_list,name='dog-list'), # register url of dog_list
    path('pet-detail/<int:pk>',views.pet_detail,name='pet-detail'), # register url of pet_detail <int:pk> is used for product which is in integer and pk is a primary key.
    path('search/',views.search,name='search'), # registering this url for search
    path('my_orders/',views.order_history,name='my_orders'),   
]   