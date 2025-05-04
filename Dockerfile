FROM python:3.11-slim

# Install wkhtmltopdf and curl
RUN apt-get update && apt-get install -y \
    wkhtmltopdf curl && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy your app code
COPY app.py index.html ./

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
