from rest_framework import viewsets

from panel.models import Room, RoomType, Tenant
from panel.serializers import RoomSerializer, RoomTypeSerializer, TenantSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """Room View Set"""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    """Room Type View Set"""

    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSetwithac(viewsets.ModelViewSet):
    """Room Type View Set"""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self, *args, **kwargs):
        filter_kwargs = {
            "is_vacant": True,
            "room_type": 1
        }
        return Room.objects.filter(**filter_kwargs)


class RoomViewSetwithoutac(viewsets.ModelViewSet):
    """Room Type View Set"""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self, *args, **kwargs):
        filter_kwargs = {
            "is_vacant": True,
            "room_type": 2
        }
        return Room.objects.filter(**filter_kwargs)


class TenantViewSet(viewsets.ModelViewSet):
    """Tenant View Set"""

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        instance = Room.objects.get(room_number=obj.room)
        instance.is_vacant = True
        instance.save()
        return super().destroy(request, *args, **kwargs)
