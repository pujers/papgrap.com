from django.urls import path
from .views import GrapListView

app_name = 'grappen'
urlpatterns = [
    path('', GrapListView.as_view(), name='list'),
]