from django.shortcuts import render
from .models import Client, Deal, Task
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

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
    clients = Client.objects.all()  # Получение всех клиентов из базы данных
    return render(request, 'crm/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        surname = request.POST.get('surname')  # Новое поле
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        birth_date = request.POST.get('birth_date')  # Новое поле

        # Сохранение данных
        Client.objects.create(
            name=name,
            surname=surname,  # Сохраняем фамилию
            email=email,
            phone=phone,
            address=address,
            birth_date=birth_date  # Сохраняем дату рождения
        )

        # Перенаправление на список клиентов
        return redirect('client_list')

    return render(request, 'crm/add_client.html')
    
def delete_client(request, client_id):
    # Получаем клиента по ID, или возвращаем 404, если его нет
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

def edit_client(request, client_id):
    # Получаем данные клиента по ID или возвращаем 404
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.surname = request.POST.get('surname')  # Фамилия
        client.birth_date = request.POST.get('birth_date')  # Дата рождения
        client.email = request.POST.get('email')
        client.phone = request.POST.get('phone')
        client.address = request.POST.get('address')
        client.save()  # Сохраняем изменения
        return redirect('client_list')  # Переход к списку клиентов

    # Если GET-запрос, передаем данные клиента в форму для отображения
    return render(request, 'crm/edit_client.html', {'client': client})