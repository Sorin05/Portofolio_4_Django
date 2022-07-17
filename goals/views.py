from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user)
    
    if request.method == 'POST':
        goal = request.POST.get('goal')
        Goal.objects.get_or_create(body=goal, user=request.user)
        return redirect('dashboard')
    return render(request, 'goals/dashboard.html', {'goals': goals})
