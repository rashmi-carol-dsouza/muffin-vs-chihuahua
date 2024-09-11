# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies and SSH server
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y openssh-server && \
    pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Install dependencies and SSH server
RUN apt-get update && apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:Docker!' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/Port 22/Port 2222/' /etc/ssh/sshd_config

# Expose port 8000 for the Django app and 2222 for SSH
EXPOSE 8000 2222

# Start both the SSH server and the Django development server
CMD service ssh start && python manage.py runserver 0.0.0.0:8000
