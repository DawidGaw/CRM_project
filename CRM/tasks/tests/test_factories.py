from datetime import timedelta

from django.test import TestCase
from tasks.factories import TaskFactory
from tasks.models import Task


class TaskFactoryTestCase(TestCase):
    def test_create_saves_task_to_database(self) -> None:
        task = TaskFactory()

        self.assertIsNotNone(task.pk)
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())

    def test_create_batch_creates_correct_number_of_tasks(self) -> None:
        tasks = TaskFactory.create_batch(5)

        self.assertEqual(len(tasks), 5)
        self.assertEqual(Task.objects.count(), 5)

    def test_reminder_is_one_hour_before_due_date(self) -> None:
        task = TaskFactory()

        self.assertEqual(
            task.reminder,
            task.due_date - timedelta(hours=1),
        )
