from django.contrib import admin


from jobs.models import developer,Company_detail,Tag
#  Job_post,Company,File

# Register your models here.


admin.site.register(developer)
admin.site.register(Company_detail)
# admin.site.register(Company_Creat_Job)
admin.site.register(Tag)
    