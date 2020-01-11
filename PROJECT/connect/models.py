from django.db import models

# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=50)
    week = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='resources/pdfs/')

    def __str__(self):
        return self.title