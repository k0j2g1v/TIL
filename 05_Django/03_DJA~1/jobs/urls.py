from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'jobs'
urlpatterns = [
    path('past_job/',views.past_job,name='past_job'),
    path('',views.index, name='index'),

]
