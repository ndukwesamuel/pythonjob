from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from jobs.models import developer,Company_detail



class DeveloperForm(forms.ModelForm):
    class Meta:
        model= developer
        fields= '__all__'
        exclude =  ['user']

class CompanyForm(forms.ModelForm):
    class Meta:
        model= Company_detail
        fields= '__all__'
        exclude = ['Company_logo','website','Job_title','Job','Level_of_seniority','Job_description',]  

# class company_profile(forms.ModelForm):
#     class Meta:
#         models =  developer
#         fields= '__all__'
#         # exclude =  ['user']