from django.db import models

# Create your models here.
class Department(models.Model):
    D_ID=models.AutoField(primary_key=True)
    D_NAME=models.CharField(max_length=50)

class Employee(models.Model):
    E_ID=models.AutoField(primary_key=True)
    E_NAME=models.CharField(max_length=100)
    DEPARTMENT=models.CharField(max_length=100)
    DATE_OF_JOINING=models.DateField()
    PHOTOFILENAME=models.CharField(max_length=100)