from fastapi import FastAPI
import redis
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env")
app = FastAPI(title="API Python Basic", description="A basic API using FastAPI, PostgreSQL, and Redis", version="1.0.0")


print("Environment variables loaded")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/secrets")
def read_secrets():
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    redis_host = os.getenv("REDIS_HOST", "redis")
    redis_port = os.getenv("REDIS_PORT", 6379)
    
    return {
        "DB_HOST": db_host,
        "DB_NAME": db_name,
        "DB_USER": db_user,
        "DB_PASSWORD": db_password,
        "DB_PORT": os.getenv("DB_PORT"),
        "REDIS_HOST": redis_host,
        "REDIS_PORT": redis_port,
    }

@app.get("/pg")
def pg_status():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT", 5432)),
            connect_timeout=3
        )
        cur = conn.cursor()
        cur.execute("SELECT 1")
        result = cur.fetchone()
        conn.close()
        return {"PostgreSQL": result}
    except Exception as e:
        return {"error": f"Could not connect to PostgreSQL: {str(e)}"}

@app.get("/redis")
def redis_status():
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"), 
        port=int(os.getenv("REDIS_PORT", 6379)))
    r.set("key", "value")
    val = r.get("key")
    return {"Redis": val#.decode()
            }
