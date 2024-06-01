from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teamfields = ['id', 'full_name', 'status', '']