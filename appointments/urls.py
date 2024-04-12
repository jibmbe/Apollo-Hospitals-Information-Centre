from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
