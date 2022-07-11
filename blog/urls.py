from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.RoutineList.as_view(),
        name='home'
    ),
    path(
        '<slug:slug>/', views.RoutineDetail.as_view(),
        name='routine_detail',
    ),
    path(
        'like/<slug:slug>', views.RoutineLike.as_view(),
        name='routine_like'
    ),

]
