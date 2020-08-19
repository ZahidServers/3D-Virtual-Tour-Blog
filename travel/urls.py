from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about-us/', views.about, name='about'),
    path('our-policy/', views.policy, name='policy'),
    path('virtual-tour/<slug:slug>', views.VirtualTour, name='VirtualTour'),
    path('p/<slug:slug>/', views.PostDetails, name='post'),
]
