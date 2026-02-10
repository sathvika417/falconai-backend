FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run Python script that properly handles PORT environment variable
CMD ["python", "-c", "import os, subprocess, sys; port = os.environ.get('PORT', '8000'); subprocess.run([sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', port])"]
