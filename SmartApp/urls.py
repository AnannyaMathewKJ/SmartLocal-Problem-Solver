from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('water/', views.water_view, name='water'),
    path('waste/', views.waste_view, name='waste'),
    path('safety/', views.safety_view, name='safety'),
    path('lost/', views.lost_view, name='lost'),
    path('air/', views.air_view, name='air'),
    path('complaint/', views.complaint_view, name='complaint'),
    path('helpsupport/', views.help_support_view, name='helpsupport'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup_view, name='signup'),
]