from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Routine
from django.urls import reverse_lazy
from .forms import CommentForm


class RoutineList(generic.ListView):
    model = Routine
    queryset = Routine.objects.filter(status=1).order_by('-added_on')[0:6]
    paginate_by = 6
    template_name = 'index.html'


class RoutineDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.filter(status=1)
        routine = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.filter(approved=True).order_by('added_on')
        liked = False
        if routine.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "routine_detail.html",
            {
                "routine": routine,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.filter(status=1)
        routine = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.filter(approved=True).order_by('added_on')
        liked = False
        if routine.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.routine = routine
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "routine_detail.html",
            {
                "routine": routine,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
