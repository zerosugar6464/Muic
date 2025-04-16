from config import LOG, LOG_GROUP_ID
import psutil
import time
from AlexaMusic import app
from AlexaMusic.utils.database import is_on_off
from AlexaMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from AlexaMusic.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)

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