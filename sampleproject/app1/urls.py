from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home', views.home, name="home"),
    path('viewModels', views.viewModels, name="viewModels"),

]