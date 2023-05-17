from client import client


# handler of auto-comment
async def auto_comment(event):
    print(event)
    await client.send_message(entity=event.message.peer_id.channel_id, message="Ну и говно конечно",
                              comment_to=event.message)
