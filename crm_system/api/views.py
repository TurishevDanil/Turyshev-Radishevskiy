from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import User, Client, Deal, Task
# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        user_data = [{"username": user.username, "role": user.role} for user in users]
        return Response({"users": user_data})
    
class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        client_list = [
            {
                "name": client.name,
                "surname": client.surname,
                "birth_date": client.birth_date,
                "email": client.email,
                "phone": client.phone,
                "address": client.address,
            }
            for client in clients
        ]
        return Response({"clients": client_list})
    
class DealView(APIView):
    def get(self, request):
        deals = Deal.objects.all()
        deal_list = [
            {
                "client": deal.client.name + " " + deal.client.surname,  # Объединение имени и фамилии клиента
                "date": deal.date,
                "amount": deal.amount,
                "status": deal.status,
            }
            for deal in deals
        ]
        return Response({"deals": deal_list})
    
class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        task_list = [
            {
                "title": task.title,
                "description": task.description,
                "deadline": task.deadline,
                "is_completed": task.is_completed,
            }
            for task in tasks
        ]
        return Response({"tasks": task_list})