from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin


@login_required
def dashboard(request):
    """Dashboard View"""
    goals = Goal.objects.filter(user=request.user)
    if request.method == 'POST':
        goal = request.POST.get('goal')
        Goal.objects.get_or_create(body=goal, user=request.user)
        return redirect('dashboard')
    return render(request, 'goals/dashboard.html', {'goals': goals})


class GoalDeleteView(UserPassesTestMixin, DeleteView):
    """View for deleted Goal"""
    model = Goal
    success_url = '/dashboard'

    def test_func(self):
        return self.request.user == self.get_object().user


class GoalUpdateView(UserPassesTestMixin, UpdateView):
    """View for update Goal"""
    model = Goal
    fields = ['body']
    success_url = '/dashboard'

    def test_func(self):
        return self.request.user == self.get_object().user
