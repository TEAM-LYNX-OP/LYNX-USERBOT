
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
# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "โัฮทฯ ะฒฯั"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://te.legra.ph/file/05db5b237fb0a98d577bc.jpg"
pm_caption = "  __**๐ฅ๐ฅ๐ณ๐๐๐ ๐ฉ๐๐ ๐ฐ๐ ๐จ๐๐๐๐๐ฅ๐ฅ**__\n\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f"โฃโขโณโ  `ััโััะฝฯฮท:` `{version.__version__}` \n"
pm_caption += f"โฃโขโณโ  `ฮฝัััฮนฯฮท:` `{mafiaversion}`\n"
pm_caption += f"โฃโขโณโ  `ัฯโฯ:` `{sudou}`\n"
pm_caption += f"โฃโขโณโ  `ยขะฝฮฑฮทฮทัโ:` [โัฮทฯ ฯฯโฮฑััั](https://t.me/Lynx_Updates)\n"
pm_caption += f"โฃโขโณโ  `ยขััฮฑัฯั:` [๐ ๐ผ๐ฟ๐ฎ๐น๐๐ผ๐](https://t.me/MoralBoy_xD)\n"
pm_caption += f"โฃโขโณโ  `gัฯฯฯ:` [โัฮทฯ ัฯฯฯฯัั](https://t.me/LynxBot_support)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += " [๐ฅััฯฯ๐ฅ](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT) ๐น [๐โฮนยขัฮทัั๐](https://github.com/TEAM-LYNX-OP/LYNX-USERBOT/blob/main/LICENSE)"

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
