from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "client",
            "due_date",
            "status",
            "priority",
            "reminder",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "client": forms.Select(attrs={"class": "form-control"}),
            "due_date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "reminder": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
        }
