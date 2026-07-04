from datetime import timedelta

from clients.models import Client, Contact
from django.utils import timezone
from tasks.models import Task
from users.models import User

from .models import Notification


def generate_notifications(user: User) -> None:
    now = timezone.now()

    # brak kontaktu
    for client in Client.objects.filter(owner=user):
        last_contact = (
            Contact.objects.filter(client=client).order_by("-contact_date").first()
        )

        if last_contact:
            days = (now.date() - last_contact.contact_date).days

            if days >= 30:
                notification, created = Notification.objects.get_or_create(
                    key=f"no_contact_{client.id}",
                    defaults={
                        "user": user,
                        "client": client,
                        "type": "no_contact",
                        "message": (
                            f"No contact with {client.company_name} for {days} days"
                        ),
                    },
                )

                if created:
                    from .tasks import send_notification_email

                    send_notification_email.delay(notification.id)

    # follow-up
    upcoming = Contact.objects.filter(
        client__owner=user,
        next_followup__range=(now, now + timedelta(days=3)),
    ).select_related("client")

    for contact in upcoming:
        notification, created = Notification.objects.get_or_create(
            key=f"followup_{contact.id}",
            defaults={
                "user": user,
                "client": contact.client,
                "type": "followup",
                "message": f"Follow-up for {contact.client.company_name}",
            },
        )

        if created:
            from .tasks import send_notification_email

            send_notification_email.delay(notification.id)

    # overdue tasks
    tasks = Task.objects.filter(
        user=user,
        due_date__lt=now,
        status__in=["todo", "in_progress"],
    )

    for task in tasks:
        notification, created = Notification.objects.get_or_create(
            key=f"task_{task.id}",
            defaults={
                "user": user,
                "type": "overdue_task",
                "message": f"Task '{task.title}' is overdue",
            },
        )

        if created:
            from .tasks import send_notification_email

            send_notification_email.delay(notification.id)
