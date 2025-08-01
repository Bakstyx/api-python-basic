# Dockerfile for a Python application using Uvicorn
FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only poetry files first for better caching
COPY ../pyproject.toml ../poetry.lock ./

# Install dependencies (no dev dependencies)
RUN poetry install --no-root --only main

# Copy the rest of the app code
COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

