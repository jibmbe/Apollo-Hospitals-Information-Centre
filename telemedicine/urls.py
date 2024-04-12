from django.urls import path
from . import views

urlpatterns = [
    path('', views.telemedicine_appointment_list, name='telemedicine_appointment_list'),
    path('index/', views.index, name='index'),
]
