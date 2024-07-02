from django.contrib import admin
from testapp.models import Hyderabad_jobs,Banglore_jobs,Pune_jobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
   
    list_display=['date','company','title','address','email','phonenumber',]

admin.site.register(Hyderabad_jobs,HydjobsAdmin)


class BangjobsAdmin(admin.ModelAdmin):
   
    list_display=['date','company','title','address','email','phonenumber',]

admin.site.register(Banglore_jobs,BangjobsAdmin)


class PunejobsAdmin(admin.ModelAdmin):
   
    list_display=['date','company','title','address','email','phonenumber',]

admin.site.register(Pune_jobs,PunejobsAdmin)

   
