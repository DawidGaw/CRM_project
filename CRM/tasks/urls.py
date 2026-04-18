from django.urls import path

from .views import (
    TaskCreateView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    toggle_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("add/", TaskCreateView.as_view(), name="task_add"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>/toggle/", toggle_task, name="task_toggle"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
]
