from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
    
# Расширьте пользователя для добавления ролей
class User(AbstractUser):
    # Остальные пользовательские поля
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('employee', 'Сотрудник'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='раб')

    # Переопределение связей с уникальными related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='crm_user_groups',  # Уникальное имя связи
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='crm_user_permissions',  # Уникальное имя связи
        blank=True
    )

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)


class Task(models.Model):
    title = models.CharField(default="", max_length=200, verbose_name="Название задачи")
    description = models.TextField(default="", blank=True, verbose_name="Описание")
    deadline = models.DateField( verbose_name="Срок выполнения")
    is_completed = models.BooleanField( verbose_name="Выполнена")

    def __str__(self):
        return self.title