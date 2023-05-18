from database import *
from client import *
import utils

# first addition of handlers (that are already in db)
targets = utils.receive_target(db)
first_addition(targets)


# TODO: write function to add new phrases in auto-comment

# handler of main commands
@client.on(telethon.events.NewMessage(main_channel))
async def command(event):
    print(event)
    message = str(event.message.text)

    if message[0] == "!":  # if it's command

        if "add_channel" in message:  # add_channel function
            await add_channel(db, message)

        elif "help" in message:  # help function
            await client.send_message(main_channel, "Вот список всех команд, что необходимы вам для использования:\n\n"
                                                    "**!add_channel <никнейм публичного канала или ссылка на него>**\n"
                                                    "__Добавляет канал на авто-комментирование__\n\n"
                                                    "**!del_channel <никнейм канала или ссылка на него>**\n"
                                                    "__Удаляет канал из списка на авто-комментирование__\n"
                                                    "**ВНИМАНИЕ** если вы"
                                                    "вводили именно ссылку на канал,"
                                                    " то вам надо указать именно ссылку.\n\n"
                                                    "**!list_all**\n__выводит список всех подключенных каналов"
                                                    " и фраз__\n\n"
                                                    "**!add_phrase**\n__Добавляет фразу, которая после, при"
                                                    "комментировании, будет (фразы выбираются случайным образом)__\n\n"
                                                    "**!del_phrase**\n__Удаляет фразу__\n\n"
                                                    "")

        elif "del_channel" in message:  # del_channel function
            await del_channel(db, message)

        elif "add_phrase" in message:  # add_phrase function
            await add_phrase(db, message)

        elif "del_phrase" in message:  # del_phrase function
            await del_phrase(db, message)

        elif "list_all" in message:  # list function
            await list_all(db)

        else:  # unknown command
            await client.send_message(main_channel, "Unknown command")


print(client.list_event_handlers())

client.run_until_disconnected()
