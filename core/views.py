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


class HabitTrackerCreate(LoginRequiredMixin, CreateView):
    model = HabitTracker
    fields = ['habit_name', 'habit_description', 'habit_numtarget', 'date_recorded', 'owner']

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('habit-detail', kwargs = {'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HabitTrackerCreate, self).get_context_data(**kwargs)
        context['habit'] = get_object_or_404(HabitTracker, pk = self.kwargs['pk'])
        return context
