from django.conf import settings
from django.db import models


class ClientNote(models.Model):
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="notes",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="client_notes",
    )

    content = models.TextField()
    tags = models.ManyToManyField("clients.Tag", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Note for {self.client}"
