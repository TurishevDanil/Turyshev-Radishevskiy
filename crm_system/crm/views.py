from django.shortcuts import render
from .models import Client, Deal, Task
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from rest_framework import viewsets
from .models import Client
from .Serializer_clients import ClientSerializer
from rest_framework.views import APIView, Response
from .Serializer_tasks import TaskSerializer



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

def task(request):
    task = Task.objects.all()
    return render(request, 'crm/task.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        description = request.POST.get('task-desc', '')
        deadline = request.POST.get('task-deadline')
        is_completed = request.POST.get('is_completed') == 'on'
        Task.objects.create(
            title=title,
            description=description,
            deadline=deadline,
            is_completed=is_completed
        )
        return redirect('task')
    
    return render(request, 'crm/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    if request.method == 'POST':
        # Приводим значение чекбокса к булевому типу
        task.is_completed = request.POST.get('is_completed') == 'on'
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.deadline = request.POST.get('deadline', task.deadline)
        
        task.save()  # Сохраняем изменения
        return redirect('task')  # Возвращаем на список задач

    return render(request, 'crm/edit_task.html', {'task': task})

# Удаление задачи
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task')  # Перенаправление на общий список задач
    


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

class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many = True)
        return Response({"clients":serializer.data})

class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response({"tasks":serializer.data})
