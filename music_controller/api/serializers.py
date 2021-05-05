from rest_framework import serializers
from .models import Room

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_skip', 'created_at')