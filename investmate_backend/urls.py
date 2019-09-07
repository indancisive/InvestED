from django.urls import path
from investmate_backend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]