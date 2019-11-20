from django.contrib import admin
from django.urls import include, path

from .router import router

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]