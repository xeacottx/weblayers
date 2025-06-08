# db.py
import psycopg
from datetime import datetime

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "postgres"
DB_PORT = 5432
DB_NAME = "weblayers"

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def insert_event(timestamp, client_ip, message):
    print(f"here is our shit: {client_ip} and {message}")
    print(f"here is the full DB URI : {DB_URL}")
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO events (timestamp, client_ip, message)
                VALUES (%s, %s, %s)
                """,
                (datetime.fromtimestamp(timestamp), client_ip, message)
            )