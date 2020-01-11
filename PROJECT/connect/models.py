from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    studentid = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank= True, null= True)

def __str__(self): 
    return self.emailid