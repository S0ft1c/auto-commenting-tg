from utils import receive_target
from utils import receive_phrase
from .client import client
from config import main_channel


async def list_all(db):
    targets = receive_target(db)
    targets = '\n'.join(targets)
    phrases = receive_phrase(db)
    phrases = '\n'.join(phrases)
    msg = \
        f"""Все подключенные каналы:
{targets}
Все фразы, которые сейчас используются:
{phrases}"""
    await client.send_message(main_channel, message=msg)
