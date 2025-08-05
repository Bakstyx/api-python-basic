from fastapi import FastAPI
import redis
import psycopg2

app = FastAPI(title="API Python Basic", description="A basic API using FastAPI, PostgreSQL, and Redis", version="1.0.0")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pg")
def pg_status():
    conn = psycopg2.connect(host="db", dbname="mydb", user="user", password="password")
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    conn.close()
    return {"PostgreSQL": result[0]}


@app.get("/redis")
def redis_status():
    r = redis.Redis(host="redis", port=6379)
    r.set("key", "value")
    val = r.get("key")
    return {"Redis": val.decode()}
