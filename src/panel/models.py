from django.db import models
from django.utils.translation import gettext_lazy


class RoomType(models.Model):
    name = models.CharField(max_length=50, verbose_name=gettext_lazy("name"))
    price = models.CharField(max_length=50, verbose_name=gettext_lazy("price"))

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=200, verbose_name=gettext_lazy("room number"))
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name=gettext_lazy("room type"))
    is_vacant = models.BooleanField(default=True, verbose_name=gettext_lazy("is vacant"))

    def __str__(self):
        return self.room_number


class Tenant(models.Model):
    name = models.CharField(max_length=200, verbose_name=gettext_lazy("name"))
    phone = models.BigIntegerField(verbose_name=gettext_lazy("phone"))
    aadharcard = models.CharField(max_length=20, verbose_name=gettext_lazy("aadhar number"))
    room = models.OneToOneField(Room, on_delete=models.CASCADE, verbose_name=gettext_lazy("room"))

    def __str__(self):
        return self.name
