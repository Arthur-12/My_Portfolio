from django.urls import path
from . import views

urlpatterns = [
  path("DjangoApps/", views.Starting_page )#this path becomes active when DjangoApps is called
]