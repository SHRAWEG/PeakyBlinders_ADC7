from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q 
from .models import student
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def search(request):
    students = student.objects.all()
    nam = student.name
    if request.method == 'POST':
        name = request.POST['srh']
        if nam == name:
            return render(request,'searched.html', {'students': students})
        else:
            return HttpResponse("no")
        
    return render(request,'searched.html',{
        'students': students
    })    
            
