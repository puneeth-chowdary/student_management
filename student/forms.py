from django import forms
from .models import register 
class registerForms(forms.Form):

    name=forms.CharField(max_length=20)
    address=forms.CharField(max_length=50)
    clas=forms.IntegerField()
    school=forms.CharField(max_length=100)

class deleteForms(forms.Form):
    name=forms.CharField(max_length=10)
class searchform(forms.Form):
    name=forms.CharField(max_length=10)