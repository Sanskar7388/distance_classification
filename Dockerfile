# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir numpy pandas scikit-learn wandb

# Command to run the script
CMD ["python", "distance_classification.py"]
