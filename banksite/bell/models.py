from django.db import models

# Create your models here.
class Reform(models.Model):
     fname= models.CharField(max_length=250)
     dob= models.DateField()
     age= models.IntegerField()
     gender= models.CharField(max_length=50)
     contact= models.CharField(max_length=100)
     mail= models.EmailField()
     address= models.TextField()
     district= models.CharField(max_length=100)
     branch= models.CharField(max_length=100)
     type= models.CharField(max_length=100)
     material= models.CharField(max_length=100)
     def __str__(self):
          return self.name
class Register(models.Model):
     username=models.CharField(max_length=200)
     pasword=models.CharField(max_length=200)
     pasword1=models.CharField(max_length=160)
     def __str__(self):
          return self.username
class Login(models.Model):
     username=models.CharField(max_length=200)
     password=models.CharField(max_length=200)
     def __str__(self):
          return self.username
