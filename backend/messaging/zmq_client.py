"""
Every time the /api/events endpoint is hit, it will publish an event using a ZeroMQ
PUB socket. Later we'll create a SUB socket (in another process/service) to receive the events.

That'll be good for logging, async pipelines, etc.
"""
import zmq

class ZMQPublisher:
    """Create a PUB socket bound to TCP port 5555 on localhost"""
    def __init__(self, bind_addr="tcp://127.0.0.1:5555"):
        context = zmq.Context.instance()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(bind_addr)

    def publish(self, topic, message):
        self.socket.send_string(f"{topic} {message}")