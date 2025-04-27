from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    remind_time = models.DateTimeField()
    
    def __str__(self):
        return self.title
