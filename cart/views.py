from django.shortcuts import redirect, render
from .models import Cart
from petsapp.models import Pets
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.

def add_to_cart(request,id): # id is used to fetch the product id
    cart_id=request.session.session_key # this line of the code help to create session in django table session key.
    if cart_id == None:
        cart_id=request.session.create() # if cart id is not enter or create then this line of code help to create session by requesting django to create.
    pet_data=Pets.objects.get(id=id) # fetching id of the product from petapp models.py Pets and pet_data is a variable
    price=pet_data.price
    user_data=request.user # requesting user information
    Cart(cart_id=cart_id,pet=pet_data,user=user_data,totalprice=price).save()
    messages.success(request,"Item Added to Cart Successfully")
    return redirect('/')
 
def cart_home(request):
    all_item=Cart.objects.filter(user=request.user)
    flag=all_item.exists()
    return render(request,'cart/cart_home.html',{'items':all_item,'flag':flag}) # {'items':all_item,'flag':flag} is a key and a value of a dictionary
    
def cart_delete(request,id):
    cart_item=Cart.objects.get(id=id)
    cart_item.delete()
    messages.success(request,"Item Removed From Cart Successfully.")
    return redirect('cartpage') 

def update_cart(request,id):
    p=request.POST.get('price')
    q=request.POST.get('qty')
    p_id=request.POST.get('id')
    total_price=float(p) * int(q)
    Cart.objects.filter(id=p_id).update(quantity=q,totalprice=total_price)
    total_amount=Cart.objects.filter(user=request.user).aggregate(total=Sum('totalprice'))['total'] or 0.00
    return JsonResponse ({'status':True,'totalprice':total_price,'totalamount':total_amount})