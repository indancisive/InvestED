from django.urls import path
from investmate_backend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('guide/', views.guide, name='guide'),
    path('guide2/<sector>/', views.guide2, name='guide2'),
    path('results/<sector_type>/<portfolio_type>/', views.results, name='results'),
]