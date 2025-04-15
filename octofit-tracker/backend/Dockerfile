# Backend Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . /app

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run Gunicorn using JSON array syntax
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "60", "octofit_tracker.wsgi:application"]