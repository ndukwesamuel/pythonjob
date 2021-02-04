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
        return redirect('fill_job')

    context = {'form':form}
    return render(request, 'Hire_developers.html', context)

# def fill_job(request):
#     sam = request.user
#     print(sam)
#     order = Order.objects.get(user=self.request.user, ordered=False)
#     form = Company_Creat_Job_form(request.POST or None, request.FILES or None, instance=sam)
#     context= {'form':form}
#     return render(request, 'fill_job.html', context)


def file_mode(request):
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('oooo')
        form.save()
        print('oooo')

    context = {'form':form},
    return render(request, 'heir.html', context)

 
def home(request):
    jobs = Company_Creat_Job.objects.all()
    for i in jobs:
        print(i.Job)

    context =  {'jobs':jobs}
    return render(request, 'index.html',context )

def job_details(request, id_test):
    job = Company_Creat_Job.objects.get(id=id_test)
 
    context =  {'job':job}

    return render(request, 'jobdetail.html',context )



def developer_profile(request):
    form= DeveloperForm(request.POST or None, request.FILES or None)
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