from django.contrib import admin
# from apps.settings.models import Settings
from .models import *

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'email']
    