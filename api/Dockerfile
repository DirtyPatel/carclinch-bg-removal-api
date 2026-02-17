FROM python:3.12-slim

WORKDIR /app

# Copy backend + core library
COPY api/src /app/api/src
COPY core /app/core

# Install deps
RUN pip install --no-cache-dir -r /app/api/src/requirements.txt

EXPOSE 8000
CMD ["uvicorn", "api.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
