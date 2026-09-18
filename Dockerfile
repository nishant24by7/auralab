FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy full application code
COPY . .

# Expose port
EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Run Flask application
CMD ["python", "app.py"]

