# detection/urls.py

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='detection/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),  # For authentication URLs
    path('add_patient/', views.add_patient, name='add_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add_test_result/<int:patient_id>/', views.add_test_result, name='add_test_result'),
]
