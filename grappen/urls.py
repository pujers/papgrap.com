from django.urls import path
from .views import (
    GrapCreateView, GrapDetailView, GrapListView, GrapUpdateView
)

app_name = 'grappen'
urlpatterns = [
    path('update/<int:pk>/', GrapUpdateView.as_view(), name='update'),
    path('create/', GrapCreateView.as_view(), name='create'),
    path('grap/<int:pk>/', GrapDetailView.as_view(), name='detail'),
    path('', GrapListView.as_view(), name='list'),
]