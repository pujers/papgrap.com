from django.urls import path
from .views import GrapDetailView, GrapListView

app_name = 'grappen'
urlpatterns = [
    path('grap/<int:pk>/', GrapDetailView.as_view(), name='detail'),
    path('', GrapListView.as_view(), name='list'),
]