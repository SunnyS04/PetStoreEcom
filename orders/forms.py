from.models import Orders,Payment,Pets,OrderPet
from django import forms

class OrderForm(forms.ModelForm):
    state=[
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('GOA','Goa'),
        ('RJ','Rajasthan'),
        ('MH','Maharashtra'),
        ('UP','Uttar Pradesh')
    ]

    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    phone=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    address=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    state=forms.CharField(widget=forms.Select(choices=state,attrs={'class':'form-control'}))

    city=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    country=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= Orders
        fields=['first_name','last_name','phone','email','address','city','state','country']