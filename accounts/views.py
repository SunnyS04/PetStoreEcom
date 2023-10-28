from typing import Optional
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegistrationForm # importing Registration forn which has created in forms.py
from django.contrib import messages # this help to display messages
from petsapp.views import pets_list # importing from petsapp the view pets-list
from django.contrib.auth.views import LoginView,LogoutView # importing bultin loginform and logoutform provided by django

# Create your views here.

def register(request): # register is a function.
    if request.method=='GET': # if user try to fill the form by GET method.
        form=RegistrationForm() # form is variable name which we have decalre
        return render(request,'base/register.html',{'form':form}) # {'form',form} dictionary created in which 'form' is a key that can be given any thing and form is value (varibale) which we have created in line 9.
    
    if request.method=='POST': # if user try to fill the form by POST method.
        form=RegistrationForm(request.POST)
        if form.is_valid(): # this line of code help to validate the form.
            form.save() # help to save the form after validate.
            username=form.cleaned_data.get('username') # username= is a varible and 'username' is feild name which has been created in forms.py.
            messages.success(request,'Account Created Successfully for '+username) # this help to show message if user regitser form successfully.
            return redirect(pets_list) # user submit the form it will redirect to pets_list.
        else: # if user failed to filled the form this code will exceuted.
            messages.error(request,'Some Issue') # message will show if error occur.
            return render(request,"base/register.html",{'form':form})  
            
    # return render(request.base/register.html,{'form':form}) # function will return 

class MyLoginView(LoginView): # help for login builtin form
    def form_valid(self,form): 
        messages.success(self.request,"LogedIn Successfuly")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"Invalid Credentials.")
        return super().form_invalid(form) 
    

class MyLogoutView(LogoutView): # help for logout builtin form
    def get_next_page(self):
        return reverse_lazy('home') # redirect to home page by using reverse_lazy 