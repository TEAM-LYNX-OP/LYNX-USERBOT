
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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓуηχ вσт"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://te.legra.ph/file/05db5b237fb0a98d577bc.jpg"
pm_caption = "  __**🔥🔥ℓуηχ вσт ιѕ αℓινє🔥🔥**__\n\n"
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `тєℓєтнση:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `νєяѕιση:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `ѕυ∂σ:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `¢нαηηєℓ:` [ℓуηχ υρ∂αтєѕ](https://t.me/Lynx_Updates)\n"
pm_caption += f"┣•➳➠ `¢яєαтσя:` [𝗠𝗼𝗿𝗮𝗹𝗕𝗼𝘆](https://t.me/MoralBoy_xD)\n"
pm_caption += f"┣•➳➠ `gяσυρ:` [ℓуηχ ѕυρρσят](https://t.me/LynxBot_support)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥яєρσ🔥](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT) 🔹 [📜ℓι¢єηѕє📜](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT/blob/main/LICENSE)"

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
