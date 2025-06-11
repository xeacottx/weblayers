# db.py
import psycopg
import os
from datetime import datetime
from db.validate import validate_event_data

def get_db_url():
    return (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

@validate_event_data
def insert_event(event_name, timestamp, client_ip, message, *args, **kwargs):
    DB_URL = get_db_url()
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO events (timestamp, client_ip, message)
                VALUES (%s, %s, %s)
                """,
                (datetime.fromtimestamp(timestamp), client_ip, message)
            )