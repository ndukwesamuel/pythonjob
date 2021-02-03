from django.shortcuts import render,redirect
from django.contrib import  messages

from jobs.models import *
from jobs.forms import *

from django.shortcuts import render


def Hire_developers(request):
    form = CompanyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('oooo')
        form.save()
        print('oooo')

    context = {'form':form}
    return render(request, 'Hire_developers.html', context)

def file_mode(request):
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('oooo')
        form.save()
        print('oooo')

    context = {'form':form},
    return render(request, 'heir.html', context)

 
def home(request):
    return render(request, 'index.html' )


def developer_profile(request):

    return render(request, 'developer_profile.html' )


def FULL_TIME(request):
    return render(request, 'fultime.html')
def PART_TIME(request):
    return render(request, 'partime.html')
def  FREELANCE(request):
    return render(request, 'freelance.html')
def REMOTE_ALL_JOBS(request):
    return render(request,'remote.html')
def alljobs(request):
    return render(request, 'alljobs.html')