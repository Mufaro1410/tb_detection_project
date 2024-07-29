# detection/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('upload/', views.upload_image, name='upload_image'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add_test_result/<int:patient_id>/', views.add_test_result, name='add_test_result'),
]
