from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Notification


def mark_as_read(request: HttpRequest, pk: int) -> HttpResponse:
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect("dashboard")
