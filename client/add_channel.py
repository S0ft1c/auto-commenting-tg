import telethon.events
from .client import client
from config import *
from .auto_comment import auto_comment


async def add_channel(db, message):
    message = message.replace("!add_channel ", "")
    db.sql_req(f"insert into channels (channel_name) values ('{message}')")
    client.add_event_handler(auto_comment, telethon.events.NewMessage(message))
    await client.send_message(main_channel, "Добавление записи произошло успешно!")
