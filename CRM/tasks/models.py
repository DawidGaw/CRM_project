from clients.models import Client
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    due_date = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )

    reminder = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    @property
    def is_overdue(self) -> bool:
        from django.utils import timezone

        return self.due_date < timezone.now() and self.status != "done"

    class Meta:
        ordering = ["due_date"]
