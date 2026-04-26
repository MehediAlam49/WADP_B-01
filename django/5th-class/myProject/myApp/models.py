from django.db import models

# Create your models here.
class studentModel(models.Model):
    rollNO = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.rollNO+"-"+self.name+"-"+self.address