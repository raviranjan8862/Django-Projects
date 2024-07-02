from django.db import models

# Create your models here.
class Hyderabad_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class Banglore_jobs(models.Model):
   date=models.DateField()
   company=models.CharField(max_length=30)
   title=models.CharField(max_length=30)
   address=models.TextField()
   email=models.EmailField()
   phonenumber=models.BigIntegerField()


class Pune_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField() 
