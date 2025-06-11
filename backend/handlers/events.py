import tornado.web
import json
from datetime import datetime, timezone
from messaging import zmq_client
from db.sqla import insert_event

publisher = zmq_client.ZMQPublisher()

class CORSMixin:
    def set_default_headers(self):
        super().set_header("Access-Control-Allow-Origin", "*")
        super().set_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        super().set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

class EventsHandler(CORSMixin, tornado.web.RequestHandler):
    def set_default_headers(self):
        # include CORS
        super().set_default_headers()
        # then JSON content type
        super().set_header("Content-Type", "application/json")

    def get(self):
        event_name = "page_loaded"
        timestamp  = datetime.now(timezone.utc).timestamp()
        client_ip  = self.request.remote_ip
        message    = "You clicked the link, and we reached the backend!"

        event = {
            "event": event_name,
            "timestamp": timestamp,
            "client_ip": (
                    self.request.headers.get("X-Forwarded-For") or
                    self.request.remote_ip),
            "message": message
        }

        # 1. Publish to ZeroMQ
        publisher.publish("event", json.dumps(event))

        # 2. Insert into Postgres
        print(f'inserting into postgres call now')
        insert_event(event_name, timestamp, client_ip, message)

        # 3. Return JSON
        self.write(json.dumps(event))