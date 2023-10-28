from django.contrib import admin
from .models import Pets  # importing module which has been created.
from django.utils.html import format_html
from orders.models import Orders,Payment,OrderPet
from cart.models import Cart

class OrderCustom(admin.ModelAdmin):
    list_display = ['user','status']


class PaymentCustom(admin.ModelAdmin):
    list_display = ['payment_id','status']



class CustomAdmin(admin.ModelAdmin): # customizing admin pannel. 
    list_display=['name','gender','price','species','description','img_display']
    list_filter=['animal_type','gender']
    search_fields=['species','age']
    list_per_page=3 # displaying how many record should display on screen.
    def img_display(self,obj): # compulsory to display images in admin panel
        return format_html('<img src={} width="200" height="200" />',obj.image.url)
# Register your models here.
admin.site.register(Pets,CustomAdmin) # register on admin site..     
admin.site.register(Cart)
admin.site.register(Orders,OrderCustom)
admin.site.register(Payment,PaymentCustom)
admin.site.register(OrderPet)
