from django.shortcuts import render, redirect  
from .forms import StudentForm 
from .models import Student 
# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():    
                form.save()  
                return redirect('/read')   
    else:  
        form = StudentForm()  
    return render(request,'create.html',{'form':form})

def read(request):
    students = Student.objects.all()

    return render(request,'CRUD.html', {'students': students})

def edit(request, id):
    students = Student.objects.get(id=id)
    
    return render(request,'edit.html',{'students': students})

def update(request, id):  
    students = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = students)  
    if form.is_valid():  
        form.save()  
        return redirect("/read")  
    return render(request, 'edit.html', {'students': students}, )  

def delete(request, id):  
    students = Student.objects.get(id=id)  
    students.delete()  
    return redirect("/read") 