from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Customer(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name


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

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    Describe_yourself = models.TextField( blank=True)
    Location = models.CharField(max_length=200, blank=True)
 
    def __str__(self):
        return self.name





class developer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,)
    Describe_yourself = models.TextField( null=True)
    Location = models.CharField(max_length=200, null=True)
    profile_pic= models.FileField(upload_to='images/', null=True,)
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
    Company_name = models.CharField(max_length=100, null=True)
    Company_logo= models.ImageField(upload_to='images/', null=True,)
    Company_Describe = models.TextField( null=True)
    website = models.CharField(max_length=200, null=True)
    Job_title = models.CharField(max_length=100, null=True)
    Job = models.CharField(max_length=100, null=True, choices=Job_type)
    Level_of_seniority = models.CharField(max_length=100, null=True, choices=Level)
    Job_description = models.TextField(null=True)
    How_to_apply = models.TextField(null=True)
    Application_target = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=100, null=True)
    tags = models.ManyToManyField(Tag)



    def __str__(self):
        return self.Company_name

class newsletter(models.Model):
    name= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.email

class test_detail(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=100, null=True)
    Company_logo= models.ImageField(upload_to='images/', null=True,)
    Company_Describe = models.TextField( null=True)
    website = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.Company_name