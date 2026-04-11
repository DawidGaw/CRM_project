from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    tax_number = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="clients"
    )
    STATUS_CHOICES = [
        ("lead", "Lead"),
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("lost", "Lost"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="lead")
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ("call", "Call"),
        ("email", "Email"),
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

    def __str__(self):
        return f"{self.client.company_name} {self.contact_type}"

    class Meta:
        ordering = ["-contact_date", "-created_at"]
