from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Routine
from django.urls import reverse_lazy
from .forms import CommentForm


def landing(request):
    routine_list = Routine.objects.all()[:6]
    return render(request, 'blog/index.html', {'routine_list': routine_list})


class RoutineList(generic.ListView):
    model = Routine

    paginate_by = 6
    
    template_name = 'blog/routine_list.html'

class RoutineDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Routine.objects.all()
        routine = get_object_or_404(queryset, slug=slug)
        comments = routine.comments.all().order_by('added_on')
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
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
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

    def post(self, request, slug):
        routine = get_object_or_404(Routine, slug=slug)

        if routine.likes.filter(id=request.user.id).exists():
            routine.likes.remove(request.user)
        else:
            routine.likes.add(request.user)
        return HttpResponseRedirect(reverse('routine_detail', args=[slug]))


class RoutineCreateView(CreateView):
    model = Routine
    fields = ['routine_name', 'description', 'picture',]
    success_url = '/'



class RoutineUpdateView(UpdateView):
    model = Routine
    fields = ['routine_name', 'description']
    success_url = '/'
    

class RoutineDeleteView(DeleteView):
    model =Routine
    success_url ='/'