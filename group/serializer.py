from rest_framework import serializers
from .models import Week, Room, Group

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
