from django.urls import path

from . import views

urlpatterns = [

	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('FULL_TIME/', views.FULL_TIME, name="fultime"),
	path('PART_TIME/', views.PART_TIME, name="PARTTIME"),
	path('FREELANCE/', views.FREELANCE, name="FREELANCE"),
	path('REMOTE/', views.REMOTE, name="REMOTE"),
  	path('Hire_developers/', views.Hire_developers, name="Hire_developers"),
	path('developer_profile/', views.developer_profile, name='developer_profile'),
	path('clicked/', views.clicked, name='clicked'),
	path('job_detail/<str:pk_test>/', views.job_detail, name="job_detail"),
	


]