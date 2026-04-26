from django.contrib import admin
from abstractApp.models import *

# Register your models here.
class Display_User_List(admin.ModelAdmin):
    list_display=['username','userType','Education']

admin.site.register(custom_user,Display_User_List)