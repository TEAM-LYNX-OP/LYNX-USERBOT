# Credit To @Kraken_The_BadASS . Keep credit if you are going to edit it. Join @HellBot_Official


import asyncio

from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing LynxBot`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing LynxBot.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing LynxBot..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing LynxBot...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing LynxBot....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing LynxBot.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO LynxBot LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(event, 
            "Your[LynxBot](https:/t.me/LynxBot_support) is working Fine...\n       Join @LynxBot_support For Any Help......"
        )

CmdHelp("test").add_command(
  "test", None, "Test wether your bot is running or not."
).add()
