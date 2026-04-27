from django.contrib import admin
from authApp.models import *
# Register your models here.
class Display_User_List(admin.ModelAdmin):
    list_display=['username','UserType','Education']

admin.site.register(custom_model,Display_User_List)