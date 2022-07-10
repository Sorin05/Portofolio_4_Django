from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Routine
from django.urls import reverse_lazy

class RoutineList(generic.ListView):
    model = Routine
    queryset = Routine.objects.filter(status=1).order_by('-added_on')[0:6]
    paginate_by = 6
    template_name = 'index.html'


class RoutineDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.filter(staus=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.filter(approved=True).order_by('created_on')
        liked = False
        if routine.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "routine_detail.html",
            {
                "routine": routine,
                "comments": comments,
                "liked": liked
            },
        )