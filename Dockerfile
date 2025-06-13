# Base image with Python
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Gradio or Flask will use
EXPOSE 7860

# Run your Python script
CMD ["python", "classify.py"]
