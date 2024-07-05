from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💥 ⁣𓆩𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק𓆪 💥", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="💥 𝕌ᴘᴅᴀᴛ𝔼 💥", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💥 ⁣𓆩𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק𓆪 💥",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="💥 ℂᴏᴍᴍᴀɴᴅʟᴇℝ 💥", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𓊈💥🔥𝔻eͥѵeͣlͫ𐍉קeℝ🔥💥𓊉", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="💥 𝕊ᴜᴘᴘᴏʀ𝕋 💥", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="💥 𝕌ᴘᴅᴀᴛ𝔼 💥", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
