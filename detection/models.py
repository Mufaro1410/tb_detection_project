from django.db import models

# # Model to store images
# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     result = models.TextField(blank=True, null=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Image {self.id}'


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return f'Image {self.name}'

class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)
    confidence = models.FloatField()
