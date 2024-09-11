from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import ImageUploadForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from django.conf import settings  
import numpy as np
import os
from django.http import HttpResponse

def home(request):
    return render(request, 'classifier/home.html')

# Load your pre-trained TensorFlow model
model_path = os.path.join(os.path.dirname(__file__), 'my_model.h5')
model = load_model(model_path)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image file
            image_file = request.FILES['image']

            # Save the image to a local directory (without using a database)
            image_path = default_storage.save(f'uploads/{image_file.name}', image_file)
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)  # Full path to the image

            # Preprocess the image for prediction
            img = load_img(full_image_path, target_size=(150, 150))  # Resize image to 150x150
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            img_array /= 255.0  # Normalize pixel values

            # Perform the prediction using the model
            prediction = model.predict(img_array)

            # Determine if it's a Chihuahua or Muffin
            label = 'Chihuahua' if prediction[0] < 0.5 else 'Muffin'

            return render(request, 'classifier/upload_success.html', {
                'form': form,
                'image_url': default_storage.url(image_path),  # Path to the uploaded image
                'label': label,  # Prediction result
            })
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/upload.html', {'form': form})
