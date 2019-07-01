from django.contrib import admin

from core.models import HabitTracker

# admin.site.register(HabitTracker)
@admin.register(HabitTracker)
class HabitTrackerAdmin(admin.ModelAdmin):
    pass


# Register your models here.
