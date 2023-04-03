from django.contrib import admin

from panel.models import Room, RoomType, Tenant

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Tenant)
