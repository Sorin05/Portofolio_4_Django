from django.shortcuts import render
from django.views import generic
from .models import Routine


class RoutineList(generic.ListView):
    model = Routine
    queryset = Routine.objects.filter(status=1).order_by('-added_on')
    template_name = 'index.html'


class RoutineList(generic.ListView):
    """View for all workout Routines"""
    model = Routine
    queryset = Routine.objects.filter(status=1).order_by('routine_name')
    template_name = 'workout_routines.html'
    paginate_by = 6
    
