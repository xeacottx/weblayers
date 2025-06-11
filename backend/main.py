import sys
import os
import argparse
# Add the directory above /handlers to sys.path (i.e., backend/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tornado.ioloop
import tornado.web
from handlers.events import EventsHandler

def parse_args():
    p = argparse.ArgumentParser(description="WebLayers Tornado Server")
    # Define flags for each DB param
    p.add_argument("--db-user",      help="Postgres user",        default=os.getenv("DB_USER", "postgres"))
    p.add_argument("--db-password",  help="Postgres password",    default=os.getenv("DB_PASSWORD", "postgres"))
    p.add_argument("--db-host",      help="Postgres host",        default=os.getenv("DB_HOST", "localhost"))
    p.add_argument("--db-port",      help="Postgres port",        default=os.getenv("DB_PORT", "5432"))
    p.add_argument("--db-name",      help="Postgres database",    default=os.getenv("DB_NAME", "weblayers"))
    p.add_argument("--port",         help="Tornado listen port",  default=int(os.getenv("PORT", "8000")))
    return p.parse_args()

def make_app():
    return tornado.web.Application([
        (r"/api/events", EventsHandler),
    ])

if __name__ == "__main__":
    args = parse_args()
    # Export them so other modules (e.g. db) can import from os.environ if needed
    os.environ.update({
        "DB_USER":     args.db_user,
        "DB_PASSWORD": args.db_password,
        "DB_HOST":     args.db_host,
        "DB_PORT":     str(args.db_port),
        "DB_NAME":     args.db_name,
    })
    print(
        f"🗄  Using DB {args.db_user}@{args.db_host}:{args.db_port}/{args.db_name}"
    )
    app = make_app()
    app.listen(8000)
    print("Server running on http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()