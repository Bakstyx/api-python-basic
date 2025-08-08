# Docker Python API Stack

A simple FastAPI application containerized with Docker, connected to PostgreSQL and Redis using Docker Compose.

## 📦 Features

- Python + FastAPI
- PostgreSQL with persistent volume
- Redis key-value store
- Environment variable management with `.env`

## 🚀 Getting Started

```bash
docker-compose up --build
```

Access the API:

- Base: http://localhost:8000
- PostgreSQL test: http://localhost:8000/pg
- Redis test: http://localhost:8000/redis

## 📂 Project Structure

```
docker-python-api-stack/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
├── docker-compose.yml
└── README.md
```

## 🛠 Environment Variables

All configuration lives in `app/.env` and is passed to the container.

## 🗄 Volumes

PostgreSQL data is persisted using the Docker volume `pgdata`.

## 🧹 Cleanup

```bash
docker-compose down -v  # remove containers, networks, and volumes
```
