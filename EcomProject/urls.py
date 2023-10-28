"""
URL configuration for EcomProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # include is compulsory for connecting urls.py file
from django.conf import settings # compulsory to display images in admin panel
from django.conf.urls.static import static # compulsory to display images in admin panel
from accounts.views import register,MyLoginView,MyLogoutView # importing the view (register) which we have created in views.py of accounts
from petsapp.views import pets_list
 
urlpatterns = [
    path('',pets_list,name='home'), # this help if user ipen to site then direct the homepage will open
    path('admin/', admin.site.urls), 
    path('petsapp/',include('petsapp.urls')), # connecting parent (EcomProject) urls.py with petsapp urls.py
    path('register/',register,name='register-page'), # registering the url 
    path('login/',MyLoginView.as_view(template_name="base/login.html"),name='login'), # the syntax is written when in vews.py code is written in class based viewd.
    path('logout/',MyLogoutView.as_view(),name='logout'),
    path('cart/',include('cart.urls'),name='cart'),
    path('orders/',include('orders.urls')),
]

if settings: #compulsory to display images in admin panel
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)