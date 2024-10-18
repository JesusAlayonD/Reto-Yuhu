from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_tasks(request):
    return render(request, 'create_tasks.html')

def read_tasks(request):
    return render(request, 'read_tasks.html')

def edit_tasks(request):
    return render(request, 'edit_tasks.html')

def delete_tasks(request):
    return render(request, 'delete_tasks.html')