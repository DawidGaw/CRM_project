from django.urls import path

from .views import DealCreateView, DealDeleteView, DealListView, DealUpdateView

urlpatterns = [
    path("", DealListView.as_view(), name="deal_list"),
    path("add/", DealCreateView.as_view(), name="deal_add"),
    path("<int:pk>/edit/", DealUpdateView.as_view(), name="deal_edit"),
    path("<int:pk>/delete/", DealDeleteView.as_view(), name="deal_delete"),
]
