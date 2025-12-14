from django.urls import path
from .views import todo_list, delete_todo, complete_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('complete/<int:todo_id>/', complete_todo, name='complete_todo'),
]