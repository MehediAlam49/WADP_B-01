from django.db import models

# Create your models here.
class bookModel(models.Model):
    BookName=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Publish_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Author