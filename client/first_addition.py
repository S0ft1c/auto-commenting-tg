from .client import client
from .auto_comment import auto_comment
import telethon.events


def first_addition(targets):
    for target in targets:
        client.add_event_handler(auto_comment, telethon.events.NewMessage(target))
