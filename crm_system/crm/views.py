from django.shortcuts import render
from .models import Client, Deal, Task, User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required
from rest_framework import  generics
from .models import Client
from .Serializer_clients import ClientSerializer
from rest_framework.views import APIView, Response
from .Serializer_tasks import TaskSerializer
from django.http import Http404
from .Serializer_deals import DealSerializer
from .Serializer_users import UserSerializer
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



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



# class TaskView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     def perform_create(self, serializer):
#         task = get_object_or_404(Task, id=self.request.data.get('task_id'))
#         return serializer.save(task=task)
    
# class SingleTaskView(RetrieveUpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class SingleTaskView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer



# class UserView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def perform_create(self, serializer):
#         user = get_object_or_404(User, id=self.request.data.get('user_id'))
#         return serializer.save(user=user)
    
# class SingleUserView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SingleUserView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# class DealView(ListCreateAPIView):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer
#     def perform_create(self, serializer):
#         deal = get_object_or_404(Deal, id=self.request.data.get('deal_id'))
#         return serializer.save(deal=deal)
    
# class SingleDealView(RetrieveUpdateAPIView):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer

# class SingleUDealView(RetrieveUpdateDestroyAPIView):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer



# class ClientView(ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     def perform_create(self, serializer):
#         client = get_object_or_404(Client, id=self.request.data.get('client_id'))
#         return serializer.save(client=client)
    
# class SingleClientView(RetrieveUpdateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class SingleClientView(RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()

# class DealViewSet(viewsets.ModelViewSet):
#     serializer_class = DealSerializer
#     queryset = Deal.objects.all()

# class ClientViewSet(viewsets.ModelViewSet):
#     serializer_class = ClientSerializer
#     queryset = Client.objects.all()

# class GetClientInfoView(APIView):
#     def get(self, request):
#         # Получаем набор всех записей из таблицы Capital
#         queryset = Client.objects.all()
#         # Сериализуем извлечённый набор записей
#         serializer_for_queryset = ClientSerializer(
#             instance=queryset, # Передаём набор записей
#             many=True # Указываем, что на вход подаётся именно набор записей
#         )
#         return Response(serializer_for_queryset.data)
    

# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class DealViewSet(viewsets.ModelViewSet):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



class DealList(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    
class DealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

