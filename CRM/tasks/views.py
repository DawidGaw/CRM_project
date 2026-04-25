from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self) -> QuerySet[Task]:
        qs = Task.objects.filter(user=self.request.user)

        status = self.request.GET.get("status")
        if status:
            qs = qs.filter(status=status)

        due = self.request.GET.get("due")
        if due == "today":
            today = timezone.now().date()
            qs = qs.filter(due_date__date=today)

        return qs


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def form_valid(self, form: TaskForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> Any:
        return reverse_lazy("task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_queryset(self) -> QuerySet[Task]:
        return Task.objects.filter(user=self.request.user)

    def get_success_url(self) -> Any:
        return reverse_lazy("task_list")


def toggle_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if task.status != "done":
        task.status = "done"
    else:
        task.status = "todo"

    task.save()
    return redirect("task_list")


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

    def get_queryset(self) -> QuerySet[Task]:
        return Task.objects.filter(user=self.request.user)
