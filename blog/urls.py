from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.RoutineList.as_view(),
        name='home'
    ),
]
