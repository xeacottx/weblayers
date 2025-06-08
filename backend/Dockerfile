# backend/Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed (for psycopg2, zmq, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose port (if needed for local testing)
EXPOSE 8000

# Command to run the app
CMD ["python", "main.py"]