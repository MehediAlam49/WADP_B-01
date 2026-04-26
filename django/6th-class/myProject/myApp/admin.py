from django.contrib import admin
from myApp.models import studentModel,teacherModel

# Register your models here.
admin.site.register(studentModel)
admin.site.register(teacherModel)