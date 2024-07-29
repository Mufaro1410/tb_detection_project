# detection/forms.py

from django import forms
from .models import Patient, TestResult

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'address']

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ['patient', 'result', 'confidence']
