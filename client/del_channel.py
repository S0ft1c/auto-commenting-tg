import telethon.events
from .client import client
from config import *
from .auto_comment import *
from telethon.tl.functions.channels import LeaveChannelRequest


async def del_channel(db, message):
    try:
        message = message.replace("!del_channel ", "")
        db.sql_req(f"delete from channels where channel_name='{message}'")
        await client(LeaveChannelRequest(message))
        client.remove_event_handler(callback=auto_comment, event=telethon.events.NewMessage(message))
        await client.send_message(main_channel, "Удаление записи произошло успешно!")
    except:
        await client.send_message(main_channel, "Удаление записи не удалось... Возможно такого канала просто нет!")
