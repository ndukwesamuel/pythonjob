from django.db import models
from django.contrib.auth.models import User


Job_type= (
			('Full-time', 'Full-time'),
            ('intenship', 'intenship'),
			('part-time', 'part-time'),
			('Freelance', 'Freelance'),
            ('Temporary', 'Temporary'),
			)
    

Level= (
			('Beginner', 'Beginner'),
            ('Junior', 'Junior'),
			('Mid level', 'Mid level'),
			('Senior', 'Senior'),
        	('Lead', 'Lead'),
            ('Manager', 'Manager'),
			)
Job_search_status = (
			('I am looking for a Vue.js job', 'I am looking for a Vue.js job'),
			('Open, but not looking', 'Open, but not looking'),
            ('Not looking for a job', 'Not looking for a job'),
			) 




class developer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True, )
    email= models.CharField(max_length=100, null=True)
    Describe_yourself = models.TextField( null=True)
    Location = models.CharField(max_length=200, null=True)
    profile_pic= models.FileField(upload_to='images/', null=True,default="images/profile1.png")
    Job_preferences = models.CharField(max_length=100, null=True, choices=Job_search_status)
    Level_of_seniority = models.CharField(max_length=100, null=True, choices=Level)
    Job = models.CharField(max_length=100, null=True, choices=Job_type)
    Skill_Set = models.CharField(max_length=200, null=True)
    laguage =  models.CharField(max_length=200, null=True)
    CV= models.FileField(upload_to='files/', null=True,)
    Privacy = models.BooleanField(default=True,null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.name

class Company_detail(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name = 'text_content')
    Company_name = models.CharField(max_length=100, null=True, blank=True)
    Company_logo= models.ImageField(upload_to='images/', null=True,default="images/profile1.png", blank=True)
    Company_Describe = models.TextField( null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    Job_title = models.CharField(max_length=100, null=True, blank=True  )
    Job = models.CharField(max_length=100, null=True, choices=Job_type, blank=True)
    Level_of_seniority = models.CharField(max_length=100, null=True, choices=Level, blank=True)
    Job_description = models.TextField(null=True, blank=True)
    short_Job_description = models.CharField(max_length=100, null=True,blank=True)
    How_to_apply = models.TextField(null=True, blank=True)
    Application_target = models.CharField(max_length=200,blank=True, null=True)
    Location = models.CharField(max_length=100, null=True,blank=True )
    tags = models.ManyToManyField(Tag, blank=True,)



    def __str__(self):
        return self.Company_name

class newsletter(models.Model):
    name= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.email
