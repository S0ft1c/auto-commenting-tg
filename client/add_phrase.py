from .client import client
from config import main_channel


async def add_phrase(db, message):
    try:
        message = message.replace("!add_phrase", "")
        db.sql_req(f"insert into phrases (phrase) values('{message}')")
        await client.send_message(main_channel, "Добавление фразы прошло успешно!")
    except:
        await client.send_message(main_channel,
                                  "Добавление фразы не удалось... Я даже не знаю, что должно вызвать такой эффект!")
