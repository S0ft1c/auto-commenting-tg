import telethon
from config import *

# config data
api_id = id
api_hash = hash

# starting telethon client
client = telethon.TelegramClient('your_client', api_id, api_hash, system_version="4.16.30-vxCUSTOM")
client.start()

