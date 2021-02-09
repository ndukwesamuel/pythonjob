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
        fields= ['Company_name']
        exclude = ['Company_logo','website','Job_title','Job','Level_of_seniority','Job_description',]
    #         Company_name = models.CharField(max_length=100, null=True)
    # Company_logo= models.ImageField(upload_to='images/', null=True,)
    # Company_Describe = models.TextField( null=True)
    # website = models.CharField(max_length=200, null=True)
    # Job_title = models.CharField(max_length=100, null=True)
    # Job = models.CharField(max_length=100, null=True, choices=Job_type)
    # Level_of_seniority = models.CharField(max_length=100, null=True, choices=Level)
    # short_des = models.CharField(max_length=100, null=True)
    # Job_description = models.TextField(null=True)
    # How_to_apply = models.TextField(null=True)
    # Application_target = models.CharField(max_length=200, null=True)
    # Location = models.CharField(max_length=100, null=True)
    # tags = models.ManyToManyField(Tag)  
        widgets = {
            'Company_name': forms.TextInput(attrs={'class': 'Company_name'}),
        }
# class company_profile(forms.ModelForm):
#     class Meta:
#         models =  developer
#         fields= '__all__'
#         # exclude =  ['user']