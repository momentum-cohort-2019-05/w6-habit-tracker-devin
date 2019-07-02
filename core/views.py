from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from core.models import HabitTracker, DailyRecord
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    """View function for home page of site."""

    num_habit_names = HabitTracker.objects.all().count()
    context = {
        'num_habit_names': num_habit_names,
    }

    return render(request, 'index.html', context=context)

class HabitTrackerListView(generic.ListView):
    model = HabitTracker


class HabitTrackerDetailView(generic.DetailView):
    model = HabitTracker

@login_required        
def add_habit_tracker(request, pk):
    from core.forms import HabitTrackerForm
    from django.views.generic.edit import CreateView
    habittracker = get_object_or_404(HabitTracker, pk=pk)
    if request.method == "POST":
        form = HabitTrackerForm(request.POST)
        if form.is_valid():
            habittracker = form.save(commit=False)
            # comment.user = request.user
            habittracker.post = HabitTracker
            form.save(HabitTracker)
            return redirect('habittracker-detail', pk=pk)
    else:
        form = HabitTrackerForm()
    return render(request, 'habittracker/add_habit_tracker', {'form': form})
