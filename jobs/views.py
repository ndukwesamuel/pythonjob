from django.shortcuts import render,redirect
from django.contrib import  messages

from jobs.models import *
from jobs.forms import *

from django.shortcuts import render

 




def home(request):
    jobs = Company_detail.objects.all()
    # for i in jobs:

    #     x=i.Job_description

    #     print(x)
        # test1 = "Do you want to work on a beautiful product? And are you passionate about development and do you want to team up with colleagues who also love what they do? Stop looking and join Co..."
        # y = len(test1.split())
        # print(y)
    context =  {'jobs':jobs}
    return render(request, 'index.html',context )

def Hire_developers(request):
    form= CompanyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'form':form}
    return render(request, 'Hire_developers.html', context)


def developer_profile(request):
    dev = developer.objects.get(user=request.user)
    form= DeveloperForm(request.POST or None, request.FILES or None, instance=dev)
    if form.is_valid():
        form.save()

    context = {'form':form}
    return render(request, 'developer_profile.html', context )


def FULL_TIME(request):
    fulltime = Company_Creat_Job.objects.filter(tags__name="FULL-TIME")
    context = {'fulltime':fulltime}
    return render(request, 'fultime.html', context)
def PART_TIME(request):
    partime = Company_Creat_Job.objects.filter(tags__name="	PART-TIME")
    context = {'partime':partime}
    return render(request, 'partime.html', context)
def  FREELANCE(request):
    freelance = Company_Creat_Job.objects.filter(tags__name="FREELANCE")
    context = {'freelance':freelance}
    return render(request, 'freelance.html', context)
def REMOTE_ALL_JOBS(request):
    remote = Company_Creat_Job.objects.filter(tags__name="	REMOTE")
    context = {'remote':remote}
    return render(request,'remote.html')
def alljobs(request):

    return render(request, 'alljobs.html')