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
    if request.method == 'POST':
        name = request.POST['srh']
        
        if name:
            matches = student.objects.filter(Q(name__icontains=name) | 
                                           Q(studentid__icontains=name)) 
            if matches: 
                return render(request,'searched.html', {
                    'matches': matches
                })
            else:
                return HttpResponse("not found")     

    return render(request,'search.html',{
        'students': students
    })    
            
