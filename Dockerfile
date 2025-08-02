# Use an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all contents from your local directory to the container's working directory
COPY . .

# Expose the port on which Flask will run
EXPOSE 5000

# Command to start the Flask application
CMD ["python", "app.py"]
