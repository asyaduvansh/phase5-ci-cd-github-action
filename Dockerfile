FROM python:3.11-slim
WORKDIR /app
ENV LOG_DIR=/app/logs
RUN apt-get update && apt-get install git -y && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
CMD ["python", "src/main.py", "--check", "all"]
