# detection/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, TestResult
from .forms import PatientForm, TestResultForm
# from django.http import HttpResponse
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image as PILImage
# import os
from PIL import Image

# model = load_model('path_to_your_model.h5')  # Update with your model path

def predict_tb(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape((1, 224, 224, 3))
    prediction = model.predict(image_array)
    return prediction


def home(request):
    # images = Image.objects.all()
    return render(request, 'detection/home.html',)
    # return render(request, 'detection/home.html', {'images': images})

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = form.save()
#             result = detect_tb(new_image.image.path)
#             new_image.result = result
#             new_image.save()
#             return redirect('home')
#     else:
#         form = ImageForm()
#     return render(request, 'detection/upload.html', {'form': form})

# def detect_tb(image_path):
#     img = PILImage.open(image_path).resize((224, 224))
#     img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     prediction = model.predict(img_array)
#     if prediction[0][0] > 0.5:
#         return 'TB Detected'
#     else:
#         return 'No TB Detected'

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'detection/add_patient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'detection/patient_list.html', {'patients': patients})

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
