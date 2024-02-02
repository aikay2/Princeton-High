from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('', views.home, name='home'),
    path('success/', views.success_page, name='success'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('create_guardian/', views.create_guardian, name='create_guardian'),
]
