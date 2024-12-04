from django.shortcuts import render
from .models import Client, Deal, Task
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

def index(request):
    return render(request, 'crm/index.html')

def index2(request):
    return render(request, 'crm/index2.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

def deals(request):
    deals = Deal.objects.all()
    return render(request, 'crm/deals.html', {'deals': deals})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'crm/tasks.html', {'tasks': tasks})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

