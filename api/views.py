from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

# Create + List Reminders
class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all().order_by('remind_at')
    serializer_class = ReminderSerializer

# Retrieve, Update (reschedule), Delete Reminders
class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
