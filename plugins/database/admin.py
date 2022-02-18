import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from plugins.config import Config
from pyrogram import Client
from plugins.database.database import db
from plugins.functions.display_progress import humanbytes
from plugins.database.bcast import broadcast_handler


@Client.on_message(filters.command("status") & filters.user(Config.OWNER_ID) & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**📦 Dɪꜱᴋ ꜱɪᴢᴇ :** {total} \n\n"
             f"**📀 Uꜱᴇᴅ :** {used}({disk_usage}%) \n\n"
             f"**💿 Fʀᴇᴇ :** {free} \n\n"
             f"**🚸 Cᴘᴜ :** {cpu_usage}% × **Rᴀᴍ :** {ram_usage}%\n\n"
             f"**👨🏻‍💻 Aᴄᴛɪᴠᴇ ᴜꜱᴇʀꜱ :** `{total_users}` \n\n"
             f"**ᴘᴏᴡᴇʀᴇᴅ ʙʏ **@Disnry_Bots**,
        parse_mode="Markdown",
        quote=True
    )


@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply & ~filters.edited)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)


