from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer
from django.shortcuts import render

# Create + List Reminders
class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all().order_by('remind_at')
    serializer_class = ReminderSerializer

# Retrieve, Update (reschedule), Delete Reminders
class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

def reminders_page(request):     # links to viewing reminders
    return render(request, 'reminders.html')

def homepage(request):       # links to homepage
    return render(request, 'reminders.html')  # different homepage change html