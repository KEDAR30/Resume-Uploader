from django.contrib import admin
from django.urls import path,include
from api.views import ProfileView

urlpatterns = [
    path('resume/',ProfileView.as_view(),name='resume'),
    path('list/',ProfileView.as_view(),name='list'),

]