from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('past_job/', views.past_job),
]
