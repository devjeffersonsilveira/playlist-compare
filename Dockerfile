# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
run pip install -r src/requirements/common.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 5000

# run python playlist-compare/manage.py runserver
