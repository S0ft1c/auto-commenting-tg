from database import *
from client import *
import utils

# first addition of handlers (that are already in db)
targets = utils.receive_target(db)
first_addition(targets)


# TODO: write function that will print list of all connected channels

# handler of main commands
@client.on(telethon.events.NewMessage(main_channel))
async def command(event):
    print(event)
    message = str(event.message.text)

    if message[0] == "!":  # if it's command

        if "add_channel" in message:  # add_channel function
            await add_channel(db, message)

        elif "help" in message:  # help function
            await client.send_message(main_channel, "help")

        elif "del_channel" in message:  # del_channel function
            await del_channel(db, message)

        else:  # unknown command
            await client.send_message(main_channel, "Unknown command")


print(client.list_event_handlers())

client.run_until_disconnected()
