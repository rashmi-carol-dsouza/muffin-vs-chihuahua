from django.shortcuts import render
from django.shortcuts import render
from .forms import ImageUploadForm
from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import ImageUploadForm
from .models import ImageUpload
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World! Welcome to the Image Classifier.")



# Load your pre-trained TensorFlow model
model_path = os.path.join(os.path.dirname(__file__), 'my_model.h5')
model = load_model(model_path)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Get the path of the uploaded image
            image_path = image_instance.image.path

            # Preprocess the image for prediction
            img = load_img(image_path, target_size=(150, 150))  # Resize image to 150x150
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            img_array /= 255.0  # Normalize pixel values

            # Perform the prediction using the model
            prediction = model.predict(img_array)

            # Determine if it's a Chihuahua or Muffin
            label = 'Chihuahua' if prediction[0] < 0.5 else 'Muffin'

            # Update the instance with the prediction (optional)
            image_instance.prediction = label
            image_instance.save()

            return render(request, 'classifier/upload_success.html', {
                'form': form,
                'image_url': image_instance.image.url,  # Path to the uploaded image
                'label': label,  # Prediction result
            })
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/upload.html', {'form': form})
