from fastapi import FastAPI
import redis
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env")
app = FastAPI(title="API Python Basic", description="A basic API using FastAPI, PostgreSQL, and Redis", version="1.0.0")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pg")
def pg_status():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    conn.close()
    return {"PostgreSQL": result[0]}


@app.get("/redis")
def redis_status():
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"), 
        port=int(os.getenv("REDIS_PORT", 6379)))
    r.set("key", "value")
    val = r.get("key")
    return {"Redis": val.decode()}
