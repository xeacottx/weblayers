from dataclasses import dataclass
from functools import wraps
import ipaddress

@dataclass
class Event:
    event: str
    timestamp: float
    client_ip: str
    message: str

    def __post_init__(self):
        if not isinstance(self.event, str) or not self.event:
            raise ValueError("`event` must be a non-empty string")
        if not isinstance(self.timestamp, (int, float)) or self.timestamp < 0:
            raise ValueError("`timestamp` must be a non-negative number")
        try:
            ipaddress.ip_address(self.client_ip)
        except ValueError:
            raise ValueError(f"`client_ip` is not valid: {self.client_ip}")
        if not isinstance(self.message, str):
            raise ValueError("`message` must be a string")

def validate_event_data(func):
    """
    Decorator that validates the four event fields via the Event schema
    before calling the underlying function.
    """
    @wraps(func)
    def wrapper(event_name, timestamp, client_ip, message):
        # will raise ValueError if any field is invalid
        Event(event=event_name,
              timestamp=timestamp,
              client_ip=client_ip,
              message=message)
        return func(event_name, timestamp, client_ip, message)
    return wrapper