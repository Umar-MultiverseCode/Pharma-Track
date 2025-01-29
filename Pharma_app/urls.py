from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
     path('login/', views.login, name='login'), 
   path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard Page
    path('inventory/', views.inventory, name='inventory'), 
    path('quality-control/', views.quality_control, name='quality_control'),
    path('distribution/', views.distribution, name='distribution'),
    path('compliance/', views.compliance, name='compliance'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings, name='settings'),
]
