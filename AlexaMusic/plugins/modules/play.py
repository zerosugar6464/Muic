from pyrogram import Client, filters
from AlexaMusic import app

LOG_CHANNEL = -1001234567890  # log kanal id'si

async def send_play_log(message, song_name):
    user = message.from_user
    text = (
        f"**Play komutu kullanıldı**\n"
        f"**Kullanıcı:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**Şarkı:** {song_name}"
    )
    await app.send_message(LOG_CHANNEL, text)

@app.on_message(filters.command("play") & filters.group)
async def play_command_handler(client, message):
    if len(message.command) < 2:
        await message.reply("Lütfen şarkı ismini yazın. Örnek: /play Shape of You")
        return

    song_name = " ".join(message.command[1:])

    await message.reply(f"'{song_name}' şarkısı kuyruğa eklendi!")

    # İşte burada çağırabilirsin:
    await send_play_log(message, song_name)