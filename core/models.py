from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class HabitTracker(models.Model):
    habit_name = models.CharField(max_length=200, help_text='Enter a habit title here')
    habit_description = models.TextField(max_length=5000, help_text='Type your habit description here')
    habit_numtarget = models.IntegerField(help_text='Enter the number you want to achieve daily for this habit')
    habit_entry = models.IntegerField(help_text='Enter the number you hit for your daily habit')
    date_recorded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
# Create your models here.

    class Meta:
        ordering = ['-date_recorded']
        unique_together = [['user', 'habit_entry']]

    def get_absolute_url(self):
        """Returns the url to access a detail record for this habit tracker."""
        return reverse('habit_tracker_detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.habit_name}'