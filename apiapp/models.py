from django.db import models

# Create your models here.

class studinfo(models.Model):
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=10)
    mail=models.EmailField()