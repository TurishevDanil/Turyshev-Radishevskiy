from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
    
class User(models.Model):
    login = models.CharField(max_length=150,  default="Ваш уникальный логин")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Рекомендуется использовать Django встроенные функции для хеширования паролей

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.login})"

class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default='неизвестно')
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True, default="example@example.com")  # Добавлено default
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Deal(models.Model):
    client = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.client


class Task(models.Model):
    title = models.CharField(default="", max_length=200, verbose_name="Название задачи")
    description = models.TextField(default="", blank=True, verbose_name="Описание")
    deadline = models.DateField( verbose_name="Срок выполнения")
    is_completed = models.BooleanField( verbose_name="Выполнена")

    def __str__(self):
        return self.title