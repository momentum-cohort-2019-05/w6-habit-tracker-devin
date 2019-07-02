import datetime
from django import forms
from django.db.models import TextField
from .models import HabitTracker, DailyRecord


class HabitTrackerForm(forms.ModelForm):

    class Meta:
        model = HabitTracker
        fields = ('habit_name', 'habit_description', 'habit_numtarget', 'owner',)

class RecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ('habit', 'day_recorded', 'habit_numachieved', 'owner',)