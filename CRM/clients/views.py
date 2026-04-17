from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from .filters import ClientFilter
from .forms import ClientForm, ContactForm
from .models import Client, Contact, Tag
from .permissions import RoleRequiredMixin


class ClientListView(LoginRequiredMixin, FilterView):
    model = Client
    template_name = "clients/client_list.html"
    context_object_name = "clients"
    filterset_class = ClientFilter

    def get_queryset(self):
        user = self.request.user
        qs = Client.objects.all()

        if user.role == "sales":
            qs = qs.filter(owner=user)
        elif user.role not in ["admin", "support"]:
            qs = qs.none()

        return qs

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.distinct()


class ClientCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = reverse_lazy("client_list")

    allowed_roles = ["admin", "sales"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        tags_str = form.cleaned_data.get("tags_input", "")
        tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            form.instance.tags.add(tag)
        return response


class ClientUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/client_form.html"
    success_url = reverse_lazy("client_list")

    allowed_roles = ["admin", "sales", "support"]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if user.role in ["admin", "support"]:
            return qs
        if user.role == "sales":
            return qs.filter(owner=user)
        return qs.none()

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial["tags_input"] = ", ".join([tag.name for tag in self.object.tags.all()])
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        tags_str = form.cleaned_data.get("tags_input", "")
        tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]

        self.object.tags.clear()
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            self.object.tags.add(tag)
        return response


class ClientDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Client
    template_name = "clients/client_confirm_delete.html"
    success_url = reverse_lazy("client_list")

    allowed_roles = ["admin"]

    def get_queryset(self) -> QuerySet[Client]:
        user = self.request.user
        if user.role == "admin":
            return Client.objects.all()
        return Client.objects.none()


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/client_detail.html"
    context_object_name = "client"


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "clients/contact_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.client_id = self.kwargs["client_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("client_detail", kwargs={"pk": self.kwargs["client_id"]})


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "clients/contact_list.html"
    context_object_name = "contacts"

    def get_queryset(self):
        user = self.request.user

        if user.role == "admin" or user.role == "support":
            return Contact.objects.all()

        elif user.role == "sales":
            return Contact.objects.filter(user=user)

        return Contact.objects.none()
