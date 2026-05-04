from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# ROLE__ADMIN = 1


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("sales", "Sales"),
        ("support", "Support"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="sales")
    last_notification_check = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"


class UserSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    no_contact_days = models.IntegerField(default=7)
    followup_days = models.IntegerField(default=2)
