from django.shortcuts import render, redirect
from .forms import ResourceForm
from django.core.files.storage import FileSystemStorage
from .models import Resource

# Create your views here.
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {
        'resources': resources
    })

def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(resource_list)
    else:
        form = ResourceForm()

    return render(request, 'upload_resource.html', {
        'form': form
    })

