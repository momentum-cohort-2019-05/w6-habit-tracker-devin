from django.contrib import admin

from core.models import HabitTracker, DailyRecord, Observer

# Register your models here.

# admin.site.register(HabitTracker)
@admin.register(HabitTracker)
class HabitTrackerAdmin(admin.ModelAdmin):
    list_display = ('habit_name', 'habit_description', 'habit_numtarget', 'owner')
    fields = ['habit_name', 'habit_description', 'habit_numtarget', 'owner']


@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = ('habit', 'day_recorded', 'date_recorded', 'habit_numachieved', 'owner')
    fields = ['habit', 'day_recorded', 'date_recorded', 'habit_numachieved', 'owner']


admin.site.register(Observer)
