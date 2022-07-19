from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Routine, Comment
from .forms import CommentForm


def landing(request):
    """ Renders the workout list on home page"""
    routine_list = Routine.objects.all()[:6]
    return render(request, 'blog/index.html', {'routine_list': routine_list})


class RoutineList(generic.ListView):
    """ View to show a list of all workouts posted by admin"""
    model = Routine
    paginate_by = 6
    template_name = 'blog/routine_list.html'


class RoutineDetail(View):
    """View of the routine detail """

    def get(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.all()
        routine = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.all()
        liked = False
        if routine.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/routine_detail.html",
            {
                "routine": routine,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.all()
        routine = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.all().order_by('-added_on')
        liked = False
        if routine.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author = request.user
            comment.routine = routine
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/routine_detail.html",
            {
                "routine": routine,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RoutineLike(View):
    """View to toggle like button"""

    def post(self, request, slug):
        routine = get_object_or_404(Routine, slug=slug)

        if routine.likes.filter(id=request.user.id).exists():
            routine.likes.remove(request.user)
        else:
            routine.likes.add(request.user)
        return HttpResponseRedirect(reverse('routine_detail', args=[slug]))


class RoutineCreateView(UserPassesTestMixin, CreateView):
    """View to create a new workout"""
    model = Routine
    fields = ['routine_name', 'description', 'picture', ]
    success_url = '/'

    def test_func(self):
        return self.request.user == User.objects.get(username='admin')


class RoutineUpdateView(UserPassesTestMixin, UpdateView):
    """View of the updated workout"""
    model = Routine
    fields = ['routine_name', 'description']
    success_url = '/'

    def test_func(self):
        return self.request.user == User.objects.get(username='admin')


class RoutineDeleteView(UserPassesTestMixin, DeleteView):
    """View of deleted Workout"""
    model = Routine
    success_url = '/'

    def test_func(self):
        return self.request.user == User.objects.get(username='admin')


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    """View for deleted comment"""
    model = Comment
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author


class CommentUpdateView(UserPassesTestMixin, UpdateView):
    """View for update comments"""
    model = Comment
    fields = ['body']
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author
