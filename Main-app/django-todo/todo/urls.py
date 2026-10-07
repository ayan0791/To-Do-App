from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('clear/', views.clear_all, name='clear_all'),
]
