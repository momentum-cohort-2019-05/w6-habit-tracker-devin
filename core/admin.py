from django.contrib import admin

from core.models import HabitTracker, DailyRecord

# Register your models here.

# admin.site.register(HabitTracker)
@admin.register(HabitTracker)
class HabitTrackerAdmin(admin.ModelAdmin):
    list_display = ('habit_name', 'habit_description', 'habit_numtarget', 'date_recorded', 'owner')
    fields = ['habit_name', 'habit_description', 'habit_numtarget', 'owner']


@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = ('habit', 'habit_numachieved', 'date_recorded', 'owner')
    fields = ['habit', 'habit_numachieved', 'owner']

