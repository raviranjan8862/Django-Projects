from django.contrib import admin
from testapp.models import Movie

# Register your models here.
class MOvieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']



admin.site.register(Movie,MOvieAdmin)
