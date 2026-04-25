from collections import Counter
from datetime import timedelta
from typing import Any, Dict, cast

from deals.models import Deal
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from tasks.models import Task

from .forms import RegisterForm
from .models import User


class RegisterView(View):
    template_name = "users/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            messages.success(
                request, f"Account created for {user.username}! You can now log in."
            )
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class CustomLoginView(LoginView):
    template_name = "users/login.html"


class CustomLogoutView(LogoutView):
    next_page = "login"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        user = cast(User, self.request.user)
        now = timezone.now()

        tasks = Task.objects.filter(user=user)

        context["role"] = user.role

        context["today_tasks"] = tasks.filter(due_date__date=now.date())
        context["upcoming_tasks"] = tasks.filter(
            due_date__range=(now, now + timedelta(days=7))
        )

        context["overdue_count"] = tasks.filter(
            due_date__lt=now, status__in=["todo", "in_progress"]
        ).count()

        context["today_count"] = tasks.filter(due_date__date=now.date()).count()

        context["done_count"] = tasks.filter(status="done").count()
        context["all_tasks_count"] = tasks.count()

        deals = Deal.objects.filter(owner=user)

        context["won_deals_count"] = deals.filter(stage="won").count()

        context["total_revenue"] = (
            deals.filter(stage="won").aggregate(total=Sum("value"))["total"] or 0
        )

        stages = deals.values_list("stage", flat=True)
        counts = Counter(stages)

        labels = []
        data = []

        for key, label in Deal.STAGE_CHOICES:
            labels.append(label)
            data.append(counts.get(key, 0))

        context["deal_labels"] = labels
        context["deal_counts"] = data

        return context
