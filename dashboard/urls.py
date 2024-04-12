from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.health_record_detail, name='health_record_detail'),
    
]
