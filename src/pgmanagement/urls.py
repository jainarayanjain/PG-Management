from django.contrib import admin
from django.urls import include, path

v1 = [
    path("panel/", include("panel.urls")),
]

apis = [
    path("v1/", include(v1)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apis)),
]
