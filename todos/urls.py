from .views import hometodo,delete_todo,todo_checked
from django.urls import path


urlpatterns=[
    path("",hometodo,name='todohome'),
    path("delete/<int:pk>/",delete_todo,name='delete_todo'),
    path("checked/<int:pk>/",todo_checked,name='todo_check'),


]

