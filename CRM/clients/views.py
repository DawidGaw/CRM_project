from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Client
from .permissions import RoleRequiredMixin

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin' or user.is_superuser:
            return Client.objects.all()
        elif user.role == 'sales':
            return Client.objects.filter(owner=user)
        elif user.role == 'support':
            return Client.objects.all()
        return Client.objects.none()


class ClientCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Client
    fields = ['company_name', 'email', 'address', 'tax_number']
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

    allowed_roles = ['admin', 'sales']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Client
    fields = ['company_name', 'email', 'address', 'tax_number']
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

    allowed_roles = ['admin', 'sales', 'support']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Client.objects.all()
        elif user.role == 'sales':
            return Client.objects.filter(owner=user)
        elif user.role == 'support':
            return Client.objects.all()
        return Client.objects.none()


class ClientDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

    allowed_roles = ['admin']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Client.objects.all()
        return Client.objects.none()