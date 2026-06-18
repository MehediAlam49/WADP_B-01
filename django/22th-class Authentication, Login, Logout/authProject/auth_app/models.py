from django.db import models

# Create your models here.
class taskModel(models.Model):
    title=models.CharField(max_length=200, null=True)