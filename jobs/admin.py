from django.contrib import admin


from jobs.models import photo, File,developer,Company_detail,Company_Creat_Job
#  Job_post,Company,File

# Register your models here.

admin.site.register(File)
admin.site.register(photo)
admin.site.register(developer)
admin.site.register(Company_detail)
admin.site.register(Company_Creat_Job)
    