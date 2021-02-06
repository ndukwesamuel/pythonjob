from django.contrib import admin

from jobs.models import developer,Company_detail,Tag,Customer,test_detail
#  Job_post,Company,File

# Register your models here.


admin.site.register(developer)
admin.site.register(Company_detail)
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(test_detail)
    