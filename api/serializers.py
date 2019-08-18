from rest_framework import serializers
from .models import PlayerStats

class PlayerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlayerStats
        fields=("id", "player", "session", "level", "action", "time", "state")
        readonlyfields=()