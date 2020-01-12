from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    email_id = models.EmailField()
    