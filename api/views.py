from django.shortcuts import render
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

def reminders_page(request):
    return render(request, 'reminders.html')
