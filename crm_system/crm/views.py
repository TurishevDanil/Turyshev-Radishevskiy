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

# Добавление клиента
def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Получить имя
        email = request.POST.get('email')  # Получить email
        phone = request.POST.get('phone')  # Получить телефон
        address = request.POST.get('address')  # Получить адрес
        Client.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('client_list')  # После добавления клиента переход на список клиентов
    return render(request, 'crm/client_list.html')

# Удаление клиента
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()  # Удалить клиента
        return redirect('client_list')

