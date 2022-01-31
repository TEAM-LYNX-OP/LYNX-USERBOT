
# Thanks to @D3_krish
# Porting in MafiaBot by @H1M4N5HU0P

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℒ𝒴𝒩𝒳 ℬ𝒪𝒯"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://te.legra.ph/file/05db5b237fb0a98d577bc.jpg"
pm_caption = "  __**🔥🔥𝓛𝓨𝓝𝓧 𝓑𝓞𝓣 𝓘𝓢 𝓐𝓛𝓘𝓥𝓔🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={mafia})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Channel:` [𝙻𝚢𝚗𝚡 𝚄𝚙𝚍𝚊𝚝𝚎𝚜](https://t.me/Lynx_Updates)\n"
pm_caption += f"┣•➳➠ `Creator:` [𝗠𝗼𝗿𝗮𝗹𝗕𝗼𝘆](https://t.me/MoralBoy_xD)\n"
pm_caption += f"┣•➳➠ `Group:` [Լყɳχẞσ𝜏 Sᥙρρσɾ𝜏](https://t.me/LynxBot_support)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥REPO🔥](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT) 🔹 [📜License📜](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
