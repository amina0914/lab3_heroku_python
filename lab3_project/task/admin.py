from django.contrib import admin
from .models import TheResponsible, TheTask

# Register your models here.
admin.site.register(TheTask)
admin.site.register(TheResponsible)

