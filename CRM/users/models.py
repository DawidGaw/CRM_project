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

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"
