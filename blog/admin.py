from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nomi']

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']
# Register your models here.
