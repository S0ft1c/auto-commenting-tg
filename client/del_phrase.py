from .client import client
from config import main_channel


async def del_phrase(db, message):
    try:
        message = message.replace("!del_phrase", "")
        db.sql_req(f"delete from phrases where phrase='{message}'")
        await client.send_message(main_channel, "Удаление фразы прошло успешно")
    except:
        await client.send_message(main_channel, "Удаление фразы не удалось... Возможно такой фразы просто нет!")
