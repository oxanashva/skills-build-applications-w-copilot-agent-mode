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

# Run Gunicorn
# The CMD instruction specifies the command to run the application using Gunicorn.
# Gunicorn is configured to bind to all network interfaces on the port specified by the $PORT Render's environment variable.
# A timeout of 60 seconds is set to accommodate the Render free plan's limitations.
# The WSGI application entry point is defined as 'octofit_tracker.wsgi:application'.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--timeout", "60", "octofit_tracker.wsgi:application"]