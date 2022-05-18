from django.shortcuts import render
from .models import TheResponsible, TheTask
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
)
from django.shortcuts import redirect
from django.core.paginator import Paginator


# Create your views here.
class GetAllTasksList(ListView):
    model = TheTask
    template_name = 'task/task_list_all.html'
    paginate_by = 5
    ordering = ['id']


def index(request):
    return render(request, 'task/home.html', {'title': 'Index'})


def about_view(request):
    return render(request, 'task/about.html', {'title': 'About'})


def contact_view(request):
    return render(request, 'task/contact.html', {'title': 'Contact'})
