# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional, for debugging)
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "main.py"]