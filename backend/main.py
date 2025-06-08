import sys
import os
# Add the directory above /handlers to sys.path (i.e., backend/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tornado.ioloop
import tornado.web
from handlers.events import EventsHandler

def make_app():
    return tornado.web.Application([
        (r"/api/events", EventsHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server running on http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()