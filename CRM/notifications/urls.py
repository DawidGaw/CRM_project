from django.urls import path

from .views import mark_as_read

urlpatterns = [
    path("read/<int:pk>/", mark_as_read, name="mark_notification"),
]
