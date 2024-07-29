# Make predictions
import numpy as np
import cv2
from tensorflow.keras.models import load_model 
model = load_model('tb_detection_model.h5')

def predict_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.expand_dims(image, axis=0) / 255.0
    prediction = model.predict(image)
    return 'TB Positive' if prediction[0][0] > 0.5 else 'TB Negative'

image_path = 'path_to_a_chest_xray_image.jpg'
result = predict_image(image_path)
print(f"Prediction: {result}")
