from django.urls import path

from . import views

urlpatterns = [

	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('FULL_TIME/', views.FULL_TIME, name="fultime"),
	path('PART_TIME/', views.PART_TIME, name="PARTTIME"),
	path('FREELANCE/', views.FREELANCE, name="FREELANCE"),
	path('REMOTE_ALL_JOBS/', views.REMOTE_ALL_JOBS, name="REMOTE"),
	path('alljobs/', views.alljobs, name='alljobs'),
  	path('heir/', views.heir, name="heir"),
   	path('file_mode/', views.file_mode, name='file_mode'),
    

]