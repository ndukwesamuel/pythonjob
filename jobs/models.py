from django.db import models

class photo(models.Model):
    name= models.CharField(max_length=500)

    videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)



# Create your models here.
# class Company(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     Company_logo =models.ImageField(upload_to='images/', null=True, verbose_name="")
#     website = models.CharField(max_length=100, null=True)
#     Job_description  = models.TextField()
#     date = models.DateTimeField(auto_now=True, null=True)
    
    
#     def __str__(self):
#         return self.name



# class Job_post(models.Model):
#     # company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
#     Position = models.CharField(max_length=100, null=True)
#     Job_type = models.CharField(max_length=100, null=True)
#     Level = models.TextField()
#     Job_description = models.DateTimeField(auto_now=True, null=True)
#     Application = models.CharField(max_length=100, null=True)
#     Application_target = models.CharField(max_length=100, null=True)
#     Location = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.title

# class File(models.Model):
    # name= models.CharField(max_length=500)
    # filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    # def __str__(self):
    #     return self.name + ": " + str(self.filepath)