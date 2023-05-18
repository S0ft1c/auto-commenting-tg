import telethon.events
from .client import client
from config import *
from .auto_comment import auto_comment
from telethon.tl.functions.channels import JoinChannelRequest


async def add_channel(db, message):
    message = message.replace("!add_channel ", "")
    db.sql_req(f"insert into channels (channel_name) values ('{message}')")
    try:
        await client(JoinChannelRequest(message))
        client.add_event_handler(auto_comment, telethon.events.NewMessage(message))
        await client.send_message(main_channel, "Добавление записи произошло успешно!")
    except:
        await client.send_message(main_channel, "Добавление записи было прервано ошибкой...\n"
                                                "Проверьте, возможно вы были забанены на канале и больше не можете"
                                                "вступить обратно.")
