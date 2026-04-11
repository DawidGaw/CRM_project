from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from users.models import User

from .forms import ClientForm
from .models import Client, Tag
from .permissions import RoleRequiredMixin


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/client_list.html"
    context_object_name = "clients"

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            queryset = Client.objects.all()
        elif user.role == "sales":
            queryset = Client.objects.filter(owner=user)
        elif user.role == "support":
            queryset = Client.objects.all()
        else:
            queryset = Client.objects.none()

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(company_name__icontains=search) | Q(email__icontains=search)
            )

        status = self.request.GET.get("status")
        owner = self.request.GET.get("owner")
        tags = self.request.GET.getlist("tags")
        if status:
            queryset = queryset.filter(status=status)
        if owner:
            queryset = queryset.filter(owner__id=owner)
        if tags:
            queryset = queryset.filter(tags__id__in=tags).distinct()
        return queryset

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        context["tags"] = Tag.objects.all()
        context["selected_tags"] = [str(t) for t in self.request.GET.getlist("tags")]
        return context


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
