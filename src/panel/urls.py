from django.urls import path

from panel.views import RoomTypeViewSet, TenantViewSet, RoomViewSetwithac, RoomViewSetwithoutac

urlpatterns = [
    path("price/", RoomTypeViewSet.as_view({"get": "list"}), name="price-list"),
    path("register/", TenantViewSet.as_view({"post": "create", "delete": "destroy","get": "list"}), name="register-post"),
    path("register/<int:pk>/", TenantViewSet.as_view({"delete": "destroy"}), name="register-delete"),
    path("roomswithac/", RoomViewSetwithac.as_view({"get": "list"}), name="rooms"),
    path("roomswithoutac/", RoomViewSetwithoutac.as_view({"get": "list"}), name="roomswith")

]
