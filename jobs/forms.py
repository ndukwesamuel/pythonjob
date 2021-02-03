from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from jobs.models import *



class ImageForm(forms.ModelForm):
    class Meta:
        model= photo
        fields= ["name", "videofile"]

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["name", "filepath"]
