from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ClientView, TaskView



urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index2, name='index2'),
    path('clients/', views.client_list, name='client_list'),
    path('deals/', views.deals, name='deals'),
    path('add/', views.add_task, name='add-task'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logged_out'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('task/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Редактирование задачи
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('client/', ClientView.as_view()),
    path('tasks/', TaskView.as_view()),
]