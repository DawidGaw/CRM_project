from clients.models import Client
from django.db import models
from users.models import User


class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ("call", "Call"),
        ("email", "Email"),
        ("meeting", "Meeting"),
        ("video", "Video call"),
        ("note", "Note"),
    ]
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="contacts"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES)
    contact_date = models.DateField()
    note = models.TextField(blank=True)
    next_followup = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-contact_date", "-created_at"]

    def __str__(self) -> str:
        return f"{self.client.company_name} {self.contact_type}"
