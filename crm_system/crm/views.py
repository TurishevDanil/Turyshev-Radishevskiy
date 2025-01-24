from django.shortcuts import render
from .models import Client, Deal, Task, User
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
from .Serializer_deals import DealSerializer
from .Serializer_users import UserSerializer
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateAPIView


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

def register(request):
    errors = []
    data = {}

    if request.method == "POST":
        login = request.POST.get('login')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        data = {
            "login": login,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }

        # Валидация данных
        if not login or not first_name or not last_name or not email or not password:
            errors.append("Все поля должны быть заполнены.")
        if password != confirm_password:
            errors.append("Пароли не совпадают.")
        if User.objects.filter(email=email).exists():
            errors.append("Пользователь с таким email уже существует.")
        if User.objects.filter(login=login).exists():
            errors.append("Логин уже занят.")

        # Если нет ошибок, создаём пользователя
        if not errors:
            try:
                user = User(
                    login=login,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password)
                )
                user.save()
                return redirect('login')
            except IntegrityError:
                errors.append("Произошла ошибка при сохранении данных. Попробуйте снова.")

    return render(request, 'registration/register.html', {'errors': errors, 'data': data})


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
    def post(self, request):
        client = request.data.get('clients')
 # Create an article from the above data
        serializer = ClientSerializer(data=client)
        if serializer.is_valid(raise_exception=True):
         client_saved = serializer.save()
        return Response({"success": "Client '{}' created successfully".format(client_saved.title)})

class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response({"tasks":serializer.data})
    def post(self, request):
        task = request.data.get('tasks')
 # Create an article from the above data
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
         task_saved = serializer.save()
        return Response({"success": "Task '{}' created successfully".format(task_saved.title)})
    
class DealView(APIView):
    def get(self, request):
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many = True)
        return Response({"deals":serializer.data})
    def post(self, request):
        deal = request.data.get('deals')
 # Create an article from the above data
        serializer = DealSerializer(data=deal)
        if serializer.is_valid(raise_exception=True):
         deal_saved = serializer.save()
        return Response({"success": "Deal '{}' created successfully".format(deal_saved.title)})

# class UserView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many = True)
#         return Response({"users":serializer.data})
#     def post(self, request):
#         user = request.data.get('users')
#  # Create an article from the above data
#         serializer = UserSerializer(data=user)
#         if serializer.is_valid(raise_exception=True):
#          user_saved = serializer.save()
#         return Response({"success": "Client '{}' created successfully".format(user_saved.title)})
#     def put(self, request, pk):
#         saved_user = get_object_or_404(User.objects.all(), pk=pk)
#         data = request.data.get('users')
#         serializer = UserSerializer(instance=saved_user, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             user_saved = serializer.save()
#         return Response({
#         "success": "User '{}' updated successfully".format(user_saved.title)
#         })
    
#     def delete(self, request, pk):
#         # Get object with this pk
#         user = get_object_or_404(User.objects.all(), pk=pk)
#         user.delete()
#         return Response({
#         "message": "User with id `{}` has been deleted.".format(pk)
#         }, status=204)

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user_id'))
        return serializer.save(user=user)
    
class SingleUserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


