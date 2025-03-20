from django.urls import path, include
from . import views


from django.contrib.auth import views as auth_views
from rest_framework import  serializers
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index2, name='index2'),
    path('deal/', views.deals, name='deals'),
    path('add/', views.add_task, name='add-task'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logged_out'),
    path('clientss/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('task/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    # path('client/', ClientView.as_view()),
    # path('tasks/', TaskView.as_view()),
    # path('deals/', DealView.as_view()),
    # path('users/', UserView.as_view()),
    # path('users/<int:pk>', SingleUserView.as_view()),
    # path('tasks/<int:pk>', SingleTaskView.as_view()),
    # path('deals/<int:pk>', SingleDealView.as_view()),
    # path('api/clients/', views.GetClientInfoView.as_view()),
    # path('api/deals/', views.GetDealInfoView.as_view()),
    # path('api/tasks/', views.GetTaskInfoView.as_view()),
    # path('api/users/', views.GetUserInfoView.as_view()),
    # path('users/', UserView.as_view({'get': 'list'})),
    # path('users/<int:pk>', UserView.as_view({'get': 'retrieve'})),
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),
    path('deals/', views.DealList.as_view()),
    path('deals/<int:pk>/', views.DealList.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('clients/<int:pk>/name', views.ClientHighlight.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)

