from pyrogram import Client

api_id = 123
api_hash = "123"

with Client("my_account", api_id, api_hash) as app:
    #app.send_message("me", "Greetings from **Pyrogram**!")
    for dialog in app.iter_dialogs():
    	print(dialog.chat.first_name or dialog.chat.title)