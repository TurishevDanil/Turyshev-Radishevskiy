from django.contrib import admin
from .models import User, Client, Deal, Task

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Deal)
admin.site.register(Task)