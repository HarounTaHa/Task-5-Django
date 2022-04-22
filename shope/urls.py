from django.urls import path
from .views import index

app_name = 'shope'

urlpatterns = [
    path('', index, name='index'),
]
