from django.urls import path
from . import views


urlpatterns = [
    path(
        '', views.dashboard, name='dashboard'
        
    ),
    path('update/<int:pk>/', views.GoalUpdateView.as_view(), name='update_goal'),
    path('delete/<int:pk>/', views.GoalDeleteView.as_view(), name='delete_goal'),
]
