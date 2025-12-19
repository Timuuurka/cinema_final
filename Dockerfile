FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better Docker cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Flask will listen on 5001
EXPOSE 5001

# Run application
CMD ["python", "run.py"]
