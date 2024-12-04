from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
    
# Расширьте пользователя для добавления ролей
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('employee', 'Сотрудник'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
        # Добавление уникального related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Уникальное имя связи
        blank=True)
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Уникальное имя связи
        blank=True
    )
    

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Deal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

class Task(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)