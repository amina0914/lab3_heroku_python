from django.urls import path
from .views import (
    GetAllTasksList,
)
from . import views

urlpatterns = [
    path('', views.index, name='task_home'),
    path('task/home/', views.index, name='task_home'),
    path('task/task_list_all/', GetAllTasksList.as_view(), name='task_list_all'),
    path('task/task-contact/', views.contact_view, name='task_contact'),
    path('task/task-about/', views.about_view, name='task_about'),

]
