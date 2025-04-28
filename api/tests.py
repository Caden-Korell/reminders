from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from .models import Reminder

class ReminderTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.reminder_data = {
            'title': 'Test Reminder',
            'description': 'This is a test.',
            'remind_at': timezone.now() + timezone.timedelta(days=1)
        }
        self.reminder = Reminder.objects.create(**self.reminder_data)

    def test_create_reminder(self):
        response = self.client.post('/api/reminders/', {
            'title': 'New Reminder',
            'description': 'New description',
            'remind_at': (timezone.now() + timezone.timedelta(days=2)).isoformat()
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 2)

    def test_update_reminder(self):
        new_time = timezone.now() + timezone.timedelta(days=3)
        response = self.client.put(f'/api/reminders/{self.reminder.id}/', {
            'title': self.reminder.title,
            'description': self.reminder.description,
            'remind_at': new_time.isoformat()
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.reminder.refresh_from_db()
        self.assertEqual(self.reminder.remind_at.replace(microsecond=0), new_time.replace(microsecond=0))

    def test_delete_reminder(self):
        response = self.client.delete(f'/api/reminders/{self.reminder.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reminder.objects.count(), 0)
