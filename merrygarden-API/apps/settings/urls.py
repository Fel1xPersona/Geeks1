from django.urls import path

from .views import SettingsAPIView

urlpatterns = [
    path('', SettingsAPIView.as_view(), name='settings_api')
]
