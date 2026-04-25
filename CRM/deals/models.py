from typing import Any

from clients.models import Client
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Deal(models.Model):
    STAGE_CHOICES = [
        ("lead", "Lead"),
        ("contacted", "Contacted"),
        ("meeting", "Meeting"),
        ("offer", "Offer"),
        ("won", "Won"),
        ("lost", "Lost"),
        ("stopped", "Stopped"),
    ]

    title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="deals")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default="lead")
    probability = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    expected_close_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    @property
    def is_closed(self) -> bool:
        return self.stage in ["won", "lost", "stopped"]

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.pk:
            old = Deal.objects.get(pk=self.pk)

            if old.stage in ["won", "lost"] and old.stage != self.stage:
                raise ValueError("Cannot change stage of closed deal")

        super().save(*args, **kwargs)
