from django.urls import path
from api_app.api.views import ListView, DetailView

urlpatterns = [
    path('jobs/', ListView.as_view() , name='list'),
    path('jobs/<int:pk>/', DetailView.as_view() , name='detail'),
]

