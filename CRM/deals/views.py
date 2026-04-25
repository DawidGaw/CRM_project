from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import DealForm
from .models import Deal


class DealListView(ListView):
    model = Deal
    template_name = "deals/deal_list.html"
    context_object_name = "deals"


class DealCreateView(CreateView):
    model = Deal
    form_class = DealForm
    template_name = "deals/deal_form.html"
    success_url = reverse_lazy("deal_list")

    def form_valid(self, form: DealForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DealUpdateView(UpdateView):
    model = Deal
    form_class = DealForm
    template_name = "deals/deal_form.html"
    success_url = reverse_lazy("deal_list")


class DealDeleteView(DeleteView):
    model = Deal
    template_name = "deals/deal_confirm_delete.html"
    success_url = reverse_lazy("deal_list")
