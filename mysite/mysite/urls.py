
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("mysite.urls")),
    path("admin/", admin.site.urls),
]
