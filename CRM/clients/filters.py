import django_filters
from django import forms
from django.db.models import Q, QuerySet
from users.models import User

from .models import Client, Tag


class ClientFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search by name or email"}
        ),
    )

    owner = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    status = django_filters.ChoiceFilter(
        choices=Client.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__id",
        to_field_name="id",
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Client
        fields = ["status", "owner", "tags"]

    def filter_search(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        return queryset.filter(
            Q(company_name__icontains=value) | Q(email__icontains=value)
        )
