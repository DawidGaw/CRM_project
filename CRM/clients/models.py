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
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients'
    )
    STATUS_CHOICES = [
        ('lead', 'Lead'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('lost', 'Lost'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lead')
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

