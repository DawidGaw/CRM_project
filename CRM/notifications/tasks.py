from datetime import timedelta

from celery import shared_task
from clients.models import Client
from deals.models import Deal
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.utils import timezone
from tasks.models import Task
from users.models import User

from .models import Notification
from .services import generate_notifications


@shared_task
def generate_all_notifications() -> None:
    for user in User.objects.iterator():
        generate_notifications(user)


@shared_task
def send_notification_email(notification_id: int) -> None:
    try:
        notification = Notification.objects.select_related("user").get(
            id=notification_id
        )

    except Notification.DoesNotExist:
        return
    if not notification.user.email:
        return

    send_mail(
        subject="CRM Notification",
        message=notification.message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[notification.user.email],
        fail_silently=False,
    )


@shared_task
def cleanup_old_notifications() -> int:
    threshold = timezone.now() - timedelta(days=30)

    deleted_count, _ = Notification.objects.filter(
        is_read=True,
        created_at__lt=threshold,
    ).delete()

    return deleted_count


@shared_task
def daily_sales_report() -> None:
    today = timezone.now().date()

    new_clients = Client.objects.filter(
        created_at__date=today,
    ).count()

    won_deals = Deal.objects.filter(
        stage="won",
        created_at__date=today,
    )

    won_count = won_deals.count()

    revenue = (
        won_deals.aggregate(
            total=Sum("value"),
        )["total"]
        or 0
    )

    tasks_today = Task.objects.filter(
        due_date__date=today,
    ).count()

    overdue_tasks = Task.objects.filter(
        due_date__lt=timezone.now(),
        status__in=["todo", "in_progress"],
    ).count()

    report = f"""
CRM DAILY REPORT

Date: {today}

New clients: {new_clients}
Won deals: {won_count}
Revenue: {revenue} PLN

Tasks due today: {tasks_today}
Overdue tasks: {overdue_tasks}
"""

    send_mail(
        subject=f"CRM Daily Report - {today}",
        message=report,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.DAILY_REPORT_RECIPIENTS,
        fail_silently=False,
    )
