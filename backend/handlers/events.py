import tornado.web
import json
from messaging import zmq_client
from db.sqla import insert_event

publisher = zmq_client.ZMQPublisher()

class EventsHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")

    def get(self):
        timestamp = self.request.request_time()
        client_ip = self.request.remote_ip
        message = "You clicked the link, and we reached the backend!"

        event_data = {
            "event": "page_loaded",
            "timestamp": timestamp,
            "client_ip": client_ip,
            "message": message
        }

        # 1. Publish to ZeroMQ
        publisher.publish("event", json.dumps(event_data))

        # 2. Insert into Postgres
        print(f'inserting into postgres call now')
        insert_event(timestamp, client_ip, message)

        # 3. Return JSON
        self.write(json.dumps(event_data))