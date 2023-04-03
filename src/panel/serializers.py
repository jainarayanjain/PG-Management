from rest_framework import serializers

from panel.models import Room, RoomType, Tenant


class RoomSerializer(serializers.ModelSerializer):
    """Room Serializer"""

    class Meta:
        model = Room
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    """Room Type Serializer"""

    class Meta:
        model = RoomType
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    """Tenant Serializer"""

    class Meta:
        model = Tenant
        fields = "__all__"

    def create(self, validated_data):
        instance = Room.objects.get(room_number=validated_data['room'])
        instance.is_vacant = False
        instance.save()
        return super().create(validated_data)
