from client import client
from utils import receive_phrase
from database import db
import random
from config import main_channel


# handler of auto-comment
async def auto_comment(event):
    print(event)
    phrases = receive_phrase(db)
    await client.send_message(entity=event.message.peer_id.channel_id,
                              message=phrases[random.randint(0, len(phrases) - 1)],
                              comment_to=event.message)
    await client.forward_messages(main_channel, event.message)
    await client.send_message(main_channel, "Произошла публикация!!!\n(на канале конкурентов)")
