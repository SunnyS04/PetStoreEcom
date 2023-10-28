# # use for creating django form 
# from django import forms # importing form and it has readymade form for user creation form and it is a toptional to import if to used djanngo form then it will compulsory to import.
# from django.contrib.auth.forms import UserCreationForm # importing UserCreationForm 
# from django.contrib.auth.models import User # User is model which has created auth table in (db_sqlite)

# class RegistrationForm(UserCreationForm): # RegistrationForm is a form name & UserCreationForm is a builtin form which has been imported in line num 3.
#     class Meta: # Meta is a builtin class provided by django and compulsory to used.
#         model= User # User is model which has been imported in line num 4 & User is model which we have previusly created in models.py.
#         fields =["username","email","first_name","last_name","password","password2","check"] # this is all column name
            
#     username=forms.CharField(
#         max_length=35,
#         required=True,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName...'}) # widget is a key which help us to input css
#     )

#     email=forms.CharField(
#         max_length=35,
#         required=True,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName...'}) # widget is a key which help us to input css
#     )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #auth user table 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        #_all_ if we need all columns
        fields = ['username','email','first_name','last_name','password1','password2','check'] 

    username = forms.CharField(max_length=100, 
                               required=True,    
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'User Name'}))
    
    email = forms.EmailField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email Address'}))
    
    first_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    
    password1 = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Password','type': 'password'}))
    
    password2 = forms.CharField(max_length=100, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Confirm Password','type': 'password'}))

    check = forms.BooleanField(required=True)