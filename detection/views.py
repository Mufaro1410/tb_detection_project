# detection/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import numpy as np
# from tensorflow.keras.models import load_model
from PIL import Image

from .models import Patient, TestResult
from .forms import PatientForm, TestResultForm

# model = load_model('path_to_your_model.h5')  # Update with your model path

def predict_tb(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape((1, 224, 224, 3))
    prediction = model.predict(image_array)
    return prediction


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'detection/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    # images = Image.objects.all()
    return render(request, 'detection/home.html',)
    # return render(request, 'detection/home.html', {'images': images})

@login_required
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'detection/add_patient.html', {'form': form})

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'detection/patient_list.html', {'patients': patients})

@login_required
def add_test_result(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == "POST":
        form = TestResultForm(request.POST)
        if form.is_valid():
            test_result = form.save(commit=False)
            test_result.patient = patient
            # Use the model to make a prediction
            result, confidence = predict_tb(request.FILES['xray_image'])
            test_result.result = result
            test_result.confidence = confidence
            test_result.save()
            return redirect('patient_list')
    else:
        form = TestResultForm()
    return render(request, 'detection/add_test_result.html', {'form': form, 'patient': patient})
