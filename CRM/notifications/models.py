from django.conf import settings
from django.db import models


class Notification(models.Model):
    TYPE_CHOICES = [
        ("no_contact", "No contact"),
        ("followup", "Follow-up"),
        ("overdue_task", "Overdue task"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, null=True, blank=True
    )
    key = models.CharField(max_length=255, unique=True)

    message = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message[:50]
