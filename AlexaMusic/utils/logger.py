import os
from config import LOG, LOG_GROUP_ID
from AlexaMusic import app

async def send_play_log(message, song_name: str):
    if not (LOG and LOG_GROUP_ID):
        return

    user = message.from_user
    chat = message.chat

    chat_link = f"@{chat.username}" if chat.username else "Özel Grup"

    log_text = f"""
**Yeni Müzik Oynatıldı**

👤 **Kullanıcı:** {user.mention}
🔢 **ID:** `{user.id}`
🏷️ **Kullanıcı Adı:** @{user.username or "Yok"}

📌 **Grup:** {chat.title}
🆔 **Grup ID:** `{chat.id}`
🔗 **Grup Linki:** {chat_link}

🎶 **Parça:** `{song_name}`
"""

    try:
        await app.send_message(LOG_GROUP_ID, log_text)
    except Exception as e:
        print(f"Log mesajı gönderilemedi: {e}")