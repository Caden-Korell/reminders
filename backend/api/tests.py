from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Reminder

class ReminderTests(APITestCase):
    def test_create_reminder(self):
        response = self.client.post('/reminders/', {'title': 'Test Reminder', 'remind_time': '2023-10-10T10:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_reminder(self):
        reminder = Reminder.objects.create(title='Delete Me', remind_time='2023-10-10T10:00:00Z')
        response = self.client.delete(f'/reminders/{reminder.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_reschedule_reminder(self):
        reminder = Reminder.objects.create(title='Reschedule Me', remind_time='2023-10-10T10:00:00Z')
        response = self.client.patch(f'/reminders/{reminder.id}/', {'remind_time': '2023-10-11T10:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
