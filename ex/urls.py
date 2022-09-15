from django.urls import path
from . import views

urlpatterns = [
    path('ex', views.index, name='index'),
]
