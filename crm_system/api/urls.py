from django.urls import path 
from .views import UserView, ClientView,DealView, TaskView
app_name = "api" 

# app_name will help us do a reverse look-up latter. 
urlpatterns = [ 
path('user/', UserView.as_view()), 
path('client/', ClientView.as_view()), 
path('deal/', DealView.as_view()), 
path('task/', TaskView.as_view()), 
] 