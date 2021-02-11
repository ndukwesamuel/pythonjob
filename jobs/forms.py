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
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'Describe_yourself':forms.Textarea(attrs={'class': 'form-control'}),
            'Location':forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class': 'form-control'}),
            'Job_preferences':forms.Select(attrs={'class': 'form-control'}),            
            'Level_of_seniority':forms.Select(attrs={'class': 'form-control'}),            
            'Job':forms.TextInput(attrs={'class': 'form-control'}),
            'Skill_Set':forms.TextInput(attrs={'class': 'form-control'}),
            'laguage':forms.TextInput(attrs={'class': 'form-control'}),
            'CV':forms.FileInput(attrs={'class': 'form-control'}),
            'Privacy':forms.NullBooleanSelect(attrs={'class': 'form-control'}),  
            
            
        }

class CompanyForm(forms.ModelForm):

    class Meta:
        model= Company_detail
        fields=  '__all__'
        widgets = {
            'Company_name':forms.TextInput(attrs={'class': 'form-control'}),
            'Company_logo':forms.FileInput(attrs={'class': 'form-control'}),
            'Company_Describe':forms.Textarea(attrs={'class': 'form-control'}),
            'website':forms.TextInput(attrs={'class': 'form-control'}),
            'Job_title':forms.TextInput(attrs={'class': 'form-control'}),
            'Job':forms.Select(attrs={'class': 'form-control'}),
            'Level_of_seniority':forms.Select(attrs={'class': 'form-control'}),
            'Job_description':forms.Textarea(attrs={'class': 'form-control'}),
            'How_to_apply':forms.Textarea(attrs={'class': 'form-control'}),
            'Application_target':forms.TextInput(attrs={'class': 'form-control'}),
            'Location':forms.TextInput(attrs={'class': 'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class': 'form-control'}),
            
        }

