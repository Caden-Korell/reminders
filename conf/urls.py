from django.urls import path
from .views import ReminderListCreateView, ReminderDetailView, reminders_page

urlpatterns = [
    path('', reminders_page, name='view-reminders'),
    path('reminders/', ReminderListCreateView.as_view(), name='reminder-list-create'),
    path('reminders/<int:pk>/', ReminderDetailView.as_view(), name='reminder-detail'),
    path('view-reminders/', reminders_page, name='view-reminders'),
]
