from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserloginForm(forms.Form):
    
    first_name = forms.CharField(max_length = 20,required=True)
    last_name = forms.CharField(max_length = 20,required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.IntegerField(required=True)