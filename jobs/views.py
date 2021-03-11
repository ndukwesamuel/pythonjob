from django.shortcuts import render,redirect
from django.contrib import  messages
 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from jobs.models import *
from jobs.forms import *

from django.shortcuts import render
from django.contrib.auth.models import Group

 
def home(request):
    jobs = Company_detail.objects.all()

    context =  {'jobs':jobs}
    return render(request, 'index.html',context )


# @login_required(login_url='clicked')
def Hire_developers(request):

    dev = Company_detail.objects.get(user=request.user)
    form= CompanyForm(request.POST or None, request.FILES or None, instance=dev)
    if form.is_valid():
        form.save()

    context = {'form':form}
    return render(request, 'Hire_developers.html', context)

@login_required(login_url='account_login')
def developer_profile(request):
    dev = developer.objects.get(user=request.user)
    form= DeveloperForm(request.POST or None, request.FILES or None, instance=dev)
    if form.is_valid():
        form.save()
        form = DeveloperForm



    context = {'form':form, 'dev':dev}
    return render(request, 'developer_profile.html', context )

def FULL_TIME(request):
    jobs = Company_detail.objects.filter(tags__name="FULLTIME")
    for i in jobs:
        print(i.Company_name)
    status = 'FULLTIME'

    context =  {'jobs':jobs, 'status':status,}
    return render(request, 'status.html',context )


def PART_TIME(request):
    jobs = Company_detail.objects.filter(tags__name="PARTTIME")
    for i in jobs:
        print(i.Company_name)
    status = 'PART TIME'

    context =  {'jobs':jobs, 'status':status,}
    return render(request, 'status.html',context )

def FREELANCE(request):
    jobs = Company_detail.objects.filter(tags__name="FREELANCE")
    for i in jobs:
        print(i.Company_name)
    status = 'FREELANCE '

    context =  {'jobs':jobs, 'status':status,}
    return render(request, 'status.html',context )

def REMOTE(request):
    jobs = Company_detail.objects.filter(tags__name="REMOTE")
    for i in jobs:
        print(i.Company_name)
    status = 'REMOTE '

    context =  {'jobs':jobs, 'status':status,}
    return render(request, 'status.html',context )


def clicked(request):
    return render(request, 'click.html')

def job_detail(request, pk_test):
    job = Company_detail.objects.get(id=pk_test)
    print('working ')
    print(job.Company_name)

    context =  {'job':job,}
    return render(request, 'jobdetail.html', context)
