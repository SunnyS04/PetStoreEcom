from django.http import Http404
from django.shortcuts import render
from .models import Pets 
from django.db.models import Q
from orders.models import OrderPet


# Create your views here.

def pets_list(request):
    all_products=Pets.objects.all() # query created which have we learn in powershell.
    context={ # context is a variable which declare.
        'objects':all_products # putting data in dictionary.
    } 
    return render(request,'petsapp/list.html',context) # request for rendering from templates which have created in pestapp the path is given 'petsapp/list.html' and after the context is the variable which have declare above

def dog_list(request): # this function is use for showing dropdown result of a cat.
    dog_list=Pets.objects.filter(animal_type='D') # query for filtering cat data for dropdown.
    all_dog_data={ # creating dictionery for storing thw variable (cat_list)
        'objects':dog_list # creating key & value 
    } 
    return render(request,'petsapp/doglist.html',all_dog_data) # rendering the url which going to show in catlist.html.

def cat_list(request): # this function is use for showing dropdown result of a cat.
    cat_list=Pets.objects.filter(animal_type='C') # query for filtering cat data for dropdown.
    all_cat_data={ # creating dictionery for storing thw variable (cat_list)
        'objects':cat_list # creating key & value 
    }
    return render(request,'petsapp/catlist.html',all_cat_data) # rendering the url which going to show in catlist.html.

def pet_detail(request,pk): # pk is used as a primary key of a product and this function is used for displaying detail of a pet.
    query = Pets.objects.get(id=pk) # get is used for fetching single element of a function & id=pkis used to fetch the detail of the product id and query is a variable.
    context= {
        'objects':query # dictionary created
    } 
    return render(request,'petsapp/pet_detail.html',context)

def search(request): # this function help to search the product.
    if request.method =='GET': # GET is used to fetch single data.
        searched_data =request.GET.get('search') # 'search' is a column name which has been created in models.py and GET and get this both are diffrent things.
        if (len(searched_data)==0): # condition passed and searched_data is a variable which declare in line num 37.
            raise Http404 # this is a builtin error which has to import first if user submit the button without inserting any value in submit button so this eroor will show.
        else:
            query=(Q(name__icontains=searched_data) | Q(species__icontains=searched_data) | Q(breed__icontains=searched_data)) # Q has also imported above and __icontains is contain that column value.
            
            result=Pets.objects.filter(query) # filtering process and query is a varible which declare in line num 41.
            
            context ={ 
                'objects':result # dictionary created
            }

            return render(request,'petsapp/search.html',context)
    else: 
        raise Http404
    

def order_history(request):
    # user = request.user
    query = OrderPet.objects.filter(user=request.user)
    # print('62',query)
    flag = query.exists()
    status_badge_map = {
        'new':'primary',
        'pending':'warning',
        'delivered':'success',
        'cancelled':'danger'
    }


    # Retriving the Order along with associated Order Item.

    orders = OrderPet.objects.filter(user=request.user).select_related('order_id','pet').order_by('-order_id__created_at')
    # print(74,orders)
    order_group = {}
    for order in orders:
        # print("78",order)
        order_number = order.order_id.order_number  # order number.
        # print(80,order_number)
        if order_number not in order_group:
            order_group[order_number] = {
                'order_date':order.order_id.created_at.date(),
                'status':order.order_id.status,
                'status_badge_map':status_badge_map.get(order.order_id.status,'secondary'),
                'order_number':order_number,
                'grand_total':0,
                'items':[]
            }

        order_group[order_number]['grand_total'] += order.pet_price
        total_price_per_item = order.quantity * order.pet_price
        order_group[order_number]['items'].append({
            'item_name':order.pet.name,
            'item_price':order.pet_price,
            'quantity':order.quantity,
            'total_price_per_item':total_price_per_item
        })

    content = {
        'order_group':order_group.values(),
        'flag':flag
    }

    return render(request,'base/order_history.html',content)
