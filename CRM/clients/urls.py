from django.urls import path

from .views import (
    ClientCreateView,
    ClientDeleteView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
)

urlpatterns = [
    path("list/", ClientListView.as_view(), name="client_list"),
    path("create/", ClientCreateView.as_view(), name="client_create"),
    path("edit/<int:pk>/", ClientUpdateView.as_view(), name="client_edit"),
    path("delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
]
