from django.shortcuts import render
from .models import Client, Deal, Task

def index(request):
    return render(request, 'crm/index.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

def deals(request):
    deals = Deal.objects.all()
    return render(request, 'crm/deals.html', {'deals': deals})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'crm/tasks.html', {'tasks': tasks})