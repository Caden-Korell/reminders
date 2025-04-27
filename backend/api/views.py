from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

# Create & List reminders
class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

# Retrieve, Update, Delete a specific reminder
class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
