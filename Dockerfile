FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y wkhtmltopdf curl && \
    pip install flask && \
    apt-get clean

# Copy project files
COPY app.py /app/app.py
WORKDIR /app

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
