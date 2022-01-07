from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from core import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("endpoint/", views.endpoint, name="endpoint"),
]
