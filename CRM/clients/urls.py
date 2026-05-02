from django.urls import path

from .views import (
    ClientCreateView,
    ClientDeleteView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
    ContactCreateView,
    ContactListView,
    add_note,
)

urlpatterns = [
    path("list/", ClientListView.as_view(), name="client_list"),
    path("create/", ClientCreateView.as_view(), name="client_create"),
    path("edit/<int:pk>/", ClientUpdateView.as_view(), name="client_edit"),
    path("delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path(
        "<int:client_id>/contacts/add/", ContactCreateView.as_view(), name="contact_add"
    ),
    path("contacts/", ContactListView.as_view(), name="contact_list"),
    path("<int:client_id>/add-note/", add_note, name="add_note"),
]
