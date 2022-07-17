from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.landing,
        name='home'
    ),
    path(
        'all-routines/',
        views.RoutineList.as_view(),
        name='routine_list'
    ),
    path(
        '<slug:slug>/', views.RoutineDetail.as_view(),
        name='routine_detail',
    ),
    path(
        'like/<slug:slug>', views.RoutineLike.as_view(),
        name='routine_like'
    ),
    path('routine/create/', views.RoutineCreateView.as_view(), name='create_routine'),
    path('routine/update/<int:pk>/', views.RoutineUpdateView.as_view(), name='update_routine'),
    path('routine/delete/<int:pk>/', views.RoutineDeleteView.as_view(), name='delete_routine'),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
