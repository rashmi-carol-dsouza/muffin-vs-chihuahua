## Muffin or Chihuahua: Django Image Classification App
This is a Django-based web application for classifying images of muffins or dogs using a pre-trained image classification model. The application is Dockerized for easy deployment and environment management.

### Features
* Image Upload: Users can upload images for classification.
Classification Model: Pre-trained TensorFlow model to classify images as either a "Muffin" or a "Dog."
* Dockerized: Runs in a Docker container for easy setup and deployment.

### Prerequisites
Before running this project, make sure you have the following installed:

Docker (Engine and Compose)
Docker Compose (Optional, for advanced setups)

### Project Setup
Step 1: Clone the Repository
```
git clone <repository-url>
cd muffin-or-dog
```

Step 2: Build the Docker Image
Run the following command to build the Docker image from the Dockerfile:

```
docker build -t django-image-classifier .
```

This command will:

Build the Docker image and tag it as django-image-classifier.
Install all the dependencies from requirements.txt (including Django and TensorFlow).

Step 3: Run the Docker Container
Run the Docker container, exposing port 8000 and mapping your current working directory for live development:

For Linux/macOS:
```
docker run -p 8000:8000 -v "$(pwd):/app" django-image-classifier
```

For Windows:
```
docker run -p 8000:8000 -v %cd%:/app django-image-classifier
```

This will:

Map port 8000 on the container to port 8000 on your local machine.
Mount the current directory to the /app directory inside the Docker container.

Step 4: Apply Database Migrations
Once the container is running, you need to apply Django database migrations:

Get the container ID by running:

```
docker ps
```

Run migrations:

```
docker exec -it <container_id> python manage.py migrate
```

This will create the necessary database tables for your Django application.

Step 5: Access the Application
Once the container is up and running, you can access the application at:

http://localhost:8000/
http://127.0.0.1:8000/

Step 6: Upload and Classify Images
Visit the /upload/ endpoint to upload images for classification.

## Troubleshooting
* Docker Daemon Not Running
If you see an error like Cannot connect to the Docker daemon, ensure Docker is running:

On Linux:

```
sudo systemctl start docker
```

On macOS/Windows: Start Docker Desktop from the applications menu.

* Port Conflict

If you encounter a port conflict (port 8000 is already in use), you can run the container on a different port:

```
docker run -p 8000:8000 -v "$(pwd):/app" django-image-classifier
```

Then, access the app at http://localhost:8080.

Cleaning Up
To stop the running container, find the container ID:

```
docker ps
```

Stop and remove the container:

```
docker stop <container_id>
docker rm <container_id>
```

If you want to remove the image as well:

```
docker rmi django-image-classifier
```

## Environment Variables
For security purposes, sensitive information like the SECRET_KEY and ALLOWED_HOSTS should be stored in an .env file. Create an .env file in the root directory and add the following:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,0.0.0.0,localhost
```

Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.