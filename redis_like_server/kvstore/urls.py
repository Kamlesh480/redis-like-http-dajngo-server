# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_value),
    path('get/', views.get_value),
    path('del/', views.delete_value),
]