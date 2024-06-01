from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Settings
from .serializers import SettingsSerializer

# Create your views here.

class SettingsAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer