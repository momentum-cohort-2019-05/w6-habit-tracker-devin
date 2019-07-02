from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class HabitTracker(models.Model):
    habit_name = models.CharField(max_length=200, help_text='Enter a habit title here')
    habit_description = models.TextField(max_length=5000, help_text='Type your habit description here')
    habit_numtarget = models.IntegerField(help_text='Enter the number you want to achieve daily for this habit')
    date_recorded = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)    

    class Meta:
        ordering = ['-date_recorded']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this habit tracker."""
        return reverse('habittracker-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.habit_name}'


class DailyRecord(models.Model):
    day_recorded = models.IntegerField(default=1, help_text="Enter what day you are on for habit tracker (e.g. Day 1, Day 2, ...)")
    habit_numachieved = models.IntegerField(help_text='Enter the number you hit for your daily habit')
    date_recorded = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(HabitTracker, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_recorded']
        unique_together = [['owner', 'habit_numachieved']]
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.habit_numachieved} {self.date_recorded}'