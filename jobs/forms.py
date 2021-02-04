from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from jobs.models import *



class DeveloperForm(forms.ModelForm):
    class Meta:
        model= developer
        fields= '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model= Company_detail
        fields= '__all__'


# class Company_Creat_Job_form(forms.ModelForm):
#     class Meta:
#         model= Company_Creat_Job
#         fields= '__all__'