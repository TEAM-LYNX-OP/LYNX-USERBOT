#credit goes to SHINCAHN & @D3_krish

import asyncio
import random

from . import *
NUMBER = ["0"]

RAIDHU = [
      "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧 𝗦𝗕𝗦𝗘𝗘𝗘𝗘𝗘 𝗦𝗘𝗘𝗫𝗫𝗫𝗬𝗬𝗬𝗬𝗬 😘💋",
    "𝗧𝗘𝗜𝗥𝗥𝗥𝗥 𝗠𝗔𝗔𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔𝗔𝗔 𝗥𝗔𝗣𝗘𝗘𝗘𝗘𝗘𝗘 𝗞𝗥𝗞𝗘𝗘𝗘𝗘 𝗕𝗛𝗔𝗚𝗚𝗚𝗚𝗚𝗚 𝗝𝗔𝗔𝗔𝗔𝗨𝗡𝗚𝗔𝗔𝗔 👅🤣🤣",
    "𝗧𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔𝗔 𝗣𝗢𝗥𝗡 𝗛𝗨𝗕 𝗠𝗔𝗜𝗜 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗙𝗔𝗔𝗗𝗡𝗘 𝗔𝗔𝗚𝗬𝗘 𝗛𝗔𝗜 𝗕𝗘𝗧𝗜𝗖𝗛𝗢𝗗⚡️⚡️⚡️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗙𝗔𝗧𝗘𝗚𝗜 𝗞𝗜𝗨𝗞𝗜 𝗦𝗕𝗦𝗘 𝗙𝗔𝗦𝗧𝗘𝗦𝗧 𝗕𝗢𝗧 𝗔𝗔𝗚𝗔𝗬𝗔 𝗛𝗔𝗜 𝗧𝗚 𝗣𝗘😈😈⚡️",
    "𝗧𝗥𝗜𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗟𝗘𝗞𝗥 𝗕𝗛𝗔𝗚 𝗝𝗔𝗔𝗨𝗡𝗚𝗔 🤣💋𝗔𝗨𝗥 𝗫𝗫𝗫 𝗕𝗔𝗡𝗔𝗨𝗡𝗚𝗔 🤤",
    "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗜𝗧𝗡𝗔 𝗫𝗛𝗢𝗗𝗨𝗡𝗚𝗔 𝗞𝗜 𝗫𝗛𝗢𝗗𝗧𝗘 𝗫𝗛𝗢𝗗𝗧𝗘 𝗕𝗔𝗫𝗫𝗛𝗘 𝗣𝗔𝗜𝗗𝗔 𝗛𝗢 𝗝𝗔𝗔𝗬𝗘𝗡𝗚𝗘 🤣🔥",
    "𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗨𝗗𝗘𝗚𝗜 𝗕𝗘𝗧𝗘 𝗖𝗛𝗨𝗗 𝗝𝗔𝗬𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧 𝗙𝗔𝗧𝗘𝗚𝗜 𝗔𝗕💦💦🍆🍑😂",
    "𝗧𝗥𝗜𝗜 𝗕𝗔𝗔𝗔𝗣 𝗫𝗛𝗔𝗞𝗞𝗔 𝗛 𝗞𝗬𝗔 ??",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗢𝗗𝗞𝗘 𝗙𝗔𝗥𝗔𝗔𝗥 𝗛𝗢 𝗚𝗔𝗬𝗜😘😂😂😂",
    "𝗧𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗜𝗧𝗡𝗔 𝗫𝗛𝗢𝗗𝗨𝗡𝗚𝗔 𝗞𝗜 𝗫𝗛𝗨𝗧 𝗙𝗔𝗧 𝗝𝗔𝗔𝗬𝗘𝗚𝗜𝗜 🤤🤣🔥",
    "𝗔𝗣𝗡𝗜𝗜𝗜𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢𝗢 𝗣𝗔𝗜𝗗 𝗚𝗜𝗥𝗟𝗟𝗟 𝗕𝗡𝗔 𝗗𝗘𝗘𝗘𝗘 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗘 𝗚𝗨𝗕𝗕𝗔𝗥𝗘 𝗣𝗛𝗘𝗞 𝗞𝗘 𝗠𝗦𝗥𝗨𝗡𝗚𝗔 𝗧𝗨𝗝𝗛𝗘😂🤤💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗠𝗔𝗜 𝗦𝗔𝗥𝗜𝗬𝗔𝗟 𝗗𝗔𝗔𝗟 𝗞𝗘 𝗖𝗛𝗨𝗧 𝗦𝗘 𝗕𝗔𝗛𝗔𝗥 𝗡𝗜𝗞𝗔𝗟𝗨𝗡𝗚𝗔 💦🍆🍑😈",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗚𝗕 𝗥𝗢𝗔𝗗 𝗞𝗜 𝗦𝗔𝗦𝗧𝗜 𝗥𝗔𝗡𝗗𝗜 𝗛𝗔𝗜 𝗕𝗘𝗧𝗘😂💋🍑🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗕𝗣 𝗦𝗛𝗢𝗢𝗧 𝗞𝗔𝗥𝗞𝗘 𝗣𝗢𝗥𝗡𝗛𝗨𝗕 𝗣𝗘 𝗗𝗔𝗟𝗨𝗡𝗚𝗔 😝🍑😂🔥",
    "𝗔𝗔𝗝 𝗧𝗘𝗥𝗔 𝗞𝗛𝗔𝗡𝗗𝗔𝗡 𝗫𝗛𝗨𝗗𝗘𝗚𝗔 💦🍆🍑",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗣𝗘 𝗝𝗛𝗨𝗟𝗘𝗚𝗜🍆🍑😁",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗞𝗢 𝗗𝗔𝗗𝗗𝗬 𝗕𝗢𝗟𝗧𝗜 𝗛𝗔𝗜😂🤤🍑💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔 𝗚𝗔𝗡𝗚 𝗕𝗔𝗡𝗚 𝗞𝗥𝗔 𝗗𝗨𝗡𝗚𝗔 🤣🔥💋 ",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗨𝗦𝗜 𝗞𝗜 𝗫𝗛𝗨𝗧 𝗞𝗔𝗔𝗟𝗜 𝗔𝗬𝗘 𝗛𝗔𝗜 𝗧𝗘𝗥𝗜 𝗧𝗢𝗛 𝗛𝗨𝗠𝗡𝗘 𝗚𝗔𝗔𝗡𝗗 𝗙𝗔𝗔𝗗 𝗗𝗔𝗔𝗟𝗜💦🍆🍑🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗖𝗔𝗥 𝗟𝗔𝗚𝗔 𝗗𝗨𝗡𝗚𝗔 𝗞𝗜𝗗𝗗 🤣🔥",
    "𝗧𝗘𝗥𝗔 𝗕𝗔𝗔𝗣 𝗞𝗢 𝗠𝗔𝗔𝗔𝗥 𝗗𝗨𝗡𝗚𝗔𝗔𝗔𝗔 𝗕𝗔𝗫𝗫𝗛𝗘 🤣👅 ",
    "𝗧𝗘𝗥𝗜 𝗚𝗔𝗔𝗡𝗗 𝗙𝗧 𝗟𝗘 𝗧𝗨𝗞𝗗𝗘 𝗛𝗢 𝗚𝗔𝗬𝗘 𝗖𝗛𝗔𝗔𝗥 𝗔𝗕𝗘 𝗖𝗛𝗔𝗟 𝗡𝗜𝗞𝗔𝗟 𝗪𝗔𝗥𝗡𝗔 𝗜𝗧𝗡𝗔 𝗠𝗔𝗥𝗨𝗡𝗚𝗔 𝗞𝗜 𝗛𝗢 𝗝𝗔𝗜𝗘𝗚𝗔 𝗧𝗘𝗥𝗔 𝗛𝗔𝗔𝗟 𝗕𝗘𝗛𝗔𝗟😂😎😈⚡️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔𝗔𝗔 𝗠𝗘𝗥𝗞𝗢 𝗗𝗔𝗗𝗗𝗬 𝗡𝗔𝗔𝗠 𝗦𝗘 𝗣𝗨𝗞𝗔𝗥𝗘𝗘𝗘😌😂😈🍑",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗦𝗕𝗦𝗘 𝗔𝗖𝗖𝗛𝗜 𝗣𝗔𝗜𝗗 𝗚𝗜𝗥𝗟 🤤💋",
    "𝗔𝗕𝗘 𝗔𝗔𝗝 𝗧𝗘𝗥𝗜 𝗚𝗔𝗔𝗡𝗗𝗔𝗜 𝗟𝗘𝗗 𝗙𝗜𝗧 𝗞𝗔𝗥𝗨𝗡𝗚𝗔 𝗙𝗜𝗥 𝗧𝗘𝗥𝗜 𝗧𝗔𝗔𝗡𝗗 𝗖𝗛𝗔𝗠𝗔𝗞 𝗨𝗧𝗛𝗘𝗚𝗜😂🍆🍑",
    "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗦𝗔𝗦𝗧𝗔 𝗦𝗣𝗔𝗠🤣 𝗕𝗢𝗧 𝗟𝗔𝗚𝗔 𝗞𝗘 𝗦𝗣𝗔𝗠 𝗞𝗥𝗨𝗡𝗚𝗔 🤤💋",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗔𝗨𝗗𝗘 𝗣𝗘 𝗙𝗜𝗦𝗔𝗟 𝗞𝗔𝗥 𝗚𝗜𝗥 𝗚𝗔𝗬𝗜 𝗔𝗨𝗥 𝗣𝗥𝗘𝗚𝗡𝗔𝗡𝗧 𝗛𝗢 𝗚𝗔𝗬𝗜😂🍑🍆💋",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗡𝗘 𝗠𝗘𝗥𝗔 𝗡𝗨𝗠𝗕𝗘𝗥 𝗗𝗔𝗗𝗗𝗬 𝗡𝗔𝗠𝗘 𝗦𝗘 𝗦𝗔𝗩𝗘 𝗞𝗔𝗥 𝗥𝗞𝗛𝗔 𝗛𝗔𝗜🙈👻😈💋",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗢 𝗟𝗔𝗨𝗗𝗘 𝗣𝗘 𝗡𝗔𝗖𝗛𝗔𝗨𝗡𝗚𝗔 😂🍆🍑",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗞𝗜 𝗗𝗜𝗘 𝗛𝗔𝗥𝗗 𝗙𝗔𝗡 𝗛𝗔𝗜 👻🙈😂💋",
    "𝗞𝗬𝗔 𝗠𝗧𝗟𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗦𝗘 𝗣𝗘𝗛𝗟𝗘 3 𝗗𝗜𝗟𝗗𝗢 𝗔𝗨𝗥 𝗘𝗞 𝗩𝗜𝗕𝗥𝗔𝗧𝗢𝗥 𝗨𝗦𝗘 𝗞𝗔𝗥𝗧𝗜 𝗧𝗛𝗜😂🍑👻🍆💦",
    "𝗔𝗣𝗡𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗫𝗛𝗨𝗧 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗭𝗢𝗠𝗔𝗧𝗢 𝗠𝗔𝗜 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔 💋🤤🥵",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗔 𝗣𝗔𝗣𝗔 𝗞𝗔 𝗟𝗨𝗡𝗗 𝗠𝗔𝗜 𝗗𝗨𝗠 𝗡𝗔𝗛𝗜 𝗧𝗛𝗔 𝗜𝗦𝗟𝗜𝗬𝗘 𝗠𝗘𝗥𝗘 𝗦𝗘 𝗖𝗛𝗨𝗗𝗞𝗘 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗡𝗘 𝗧𝗨𝗝𝗛𝗘 𝗝𝗔𝗡𝗔𝗠 𝗗𝗜𝗬𝗔🍆💦🍑😂👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗔𝗠𝗔𝗭𝗢𝗡 𝗠𝗔𝗜 𝗦𝗘𝗟𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 50 𝗠𝗔𝗜 🤤💋😊❤️",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗢 𝗖𝗛𝗢𝗖𝗢𝗟𝗔𝗧𝗘 𝗙𝗟𝗔𝗩𝗢𝗨𝗥 𝗣𝗔𝗦𝗔𝗡𝗗 𝗛𝗔𝗜👻🍆🍑😂",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗘 𝗚𝗛𝗔𝗥 𝗞𝗘 𝗣𝗔𝗔𝗦 𝗪𝗔𝗟𝗘 𝗗𝗨𝗞𝗔𝗡 𝗠𝗔𝗜 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 200 𝗞𝗘 𝗕𝗛𝗔𝗩 𝗕𝗜𝗞 𝗥𝗛𝗜 𝗛𝗔𝗜😂👻🍆🍑",
    "𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗫𝗛𝗨𝗧 𝗦𝗕𝗦𝗘 𝗦𝗘𝗫𝗫𝗬 𝗛 𝗠𝗔𝗗𝗔𝗥𝗫𝗝𝗢𝗗 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗙𝗔𝗧 𝗞𝗘 𝗛𝗢 𝗚𝗔𝗬𝗘 𝗧𝗨𝗞𝗗𝗘 𝗖𝗛𝗔𝗔𝗥😂🍑🍆👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧 𝗙𝗔𝗔𝗔𝗗 𝗞𝗘 𝗦𝗔𝗕 𝗦𝗘 𝗖𝗛𝗨𝗗𝗪𝗔𝗡𝗨𝗡𝗚𝗔 🤤💋🔥",
    "𝗔𝗡𝗗𝗜 𝗠𝗔𝗡𝗗𝗜 𝗦𝗔𝗡𝗗𝗜 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗫𝗛𝗨𝗧𝗧𝗧😂👻🍆🍑",
    "𝗔𝗔𝗨𝗞𝗔𝗔𝗧 𝗠𝗔𝗜 𝗥𝗘𝗛 𝗞𝗔𝗥 𝗕𝗔𝗔𝗧 𝗞𝗥 𝗟𝗜𝗬𝗔 𝗞𝗥 𝗕𝗔𝗫𝗫𝗛𝗘 𝗪𝗔𝗥𝗡𝗔 𝗠𝗔𝗔𝗔 𝗫𝗛𝗢𝗗 𝗗𝗘𝗡𝗚𝗘 🤣🔥🖕",
    "𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗔 𝗟𝗨𝗡𝗗 𝗗𝗘𝗞𝗛𝗞𝗥 𝗗𝗔𝗘 𝗚𝗔𝗬𝗜 𝗗𝗔𝗥𝗞𝗘 𝗨𝗦𝗡𝗘 𝗗𝗜𝗬𝗔 𝗠𝗨𝗧 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗞𝗔𝗔𝗟𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧😂🍑👻",
    "𝗛𝗔𝗥𝗘 𝗛𝗔𝗥𝗘 𝗝𝗛𝗔𝗗𝗜𝗬𝗢 𝗠𝗘 𝗕𝗔𝗗𝗔 𝗕𝗔𝗗𝗔 𝗚𝗛𝗢𝗦𝗟𝗔 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂🍑🍆👻",
    "𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗔 𝗟𝗨𝗡𝗗 𝗗𝗘𝗞𝗛𝗞𝗥 𝗗𝗔𝗘 𝗚𝗔𝗬𝗜 𝗗𝗔𝗥𝗞𝗘 𝗨𝗦𝗡𝗘 𝗗𝗜𝗬𝗔 𝗠𝗨𝗧 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗞𝗔𝗔𝗟𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧😂🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗟𝗘𝗞𝗘 𝗕𝗛𝗔𝗚 𝗝𝗔𝗔𝗨𝗡𝗚𝗔  🤤💋𝗔𝗨𝗥 𝗞𝗔𝗟 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔  𝗗𝗜𝗞𝗛𝗘𝗚𝗜 𝗖𝗜𝗗 𝗠𝗔𝗜 🤣🔥",
    "𝗔𝗥𝗘 𝗕𝗘𝗧𝗘 CUTE KING 𝗞𝗘 𝗣𝗜𝗥𝗢 𝗕𝗢𝗧 𝗦𝗘 𝗖𝗛𝗨𝗗 𝗚𝗔𝗬𝗔 𝗧𝗨 𝗡𝗜𝗞𝗟 𝗪𝗔𝗥𝗡𝗔 𝗔𝗨𝗥 𝗖𝗛𝗨𝗗𝗘𝗚𝗔 𝗕𝗘𝗧𝗘😁🍆🔥🍑",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧 𝗟𝗘𝗔𝗞 𝗞𝗔𝗥 𝗥𝗛𝗜 𝗛𝗔𝗜 𝗠𝗔𝗜 𝗣𝗟𝗨𝗠𝗕𝗘𝗥 𝗛𝗨 𝗥𝗨𝗞 𝗧𝗛𝗜𝗞 𝗞𝗔𝗥 𝗗𝗨𝗡𝗚𝗔😂🍆🍑👻",
    "𝗔𝗡𝗗𝗜𝗜 𝗠𝗔𝗡𝗗𝗜𝗜𝗜 𝗦𝗛𝗔𝗡𝗗𝗜𝗜𝗜 𝗔𝗚𝗔𝗥 𝗗𝗨𝗦𝗠𝗔𝗡 𝗟𝗢𝗚 𝗥𝗘𝗣𝗟𝗬 𝗞𝗜𝗬𝗔 𝗧𝗢𝗛 𝗨𝗦𝗞𝗔 𝗠𝗔 𝗕𝗛𝗘𝗡 𝗥𝗔𝗡𝗗𝗜𝗜 😅😅😒",
    "𝗧𝗨 𝗔𝗨𝗥 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗖𝗔𝗥 𝗖𝗛𝗔𝗗𝗔 𝗗𝗨𝗡𝗚𝗔 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 🤣🔥",
    "𝗔𝗥𝗘 𝗝𝗬𝗔𝗗𝗔 𝗨𝗗 𝗠𝗔𝗧 𝗪𝗔𝗥𝗡𝗔 𝗣𝗛𝗢𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗔 𝗞𝗛𝗢𝗣𝗗𝗔 𝗔𝗨𝗥 𝗝𝗬𝗔𝗗𝗔 𝗕𝗢𝗟𝗘𝗚𝗔 𝗧𝗢𝗛 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗔 𝗕𝗚𝗢𝗦𝗗𝗔😂🍆🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗦𝗔𝗕 𝗞𝗢 𝗕𝗔𝗔𝗧 𝗗𝗨𝗡𝗚𝗔 🤣✌️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗢 𝗞𝗜𝗗𝗡𝗔𝗣 𝗞𝗥𝗞𝗘 𝗡𝗔𝗡𝗚𝗔 𝗥𝗢𝗔𝗗 𝗣𝗘 𝗫𝗛𝗢𝗗 𝗗𝗨𝗡𝗙𝗔 🤣🤤🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗬𝗬𝗜𝗔 𝗧𝗢𝗛 𝗞𝗔𝗟𝗔𝗣𝗡𝗘 𝗟𝗔𝗚𝗜 🤣🥺",
    "𝗔𝗕𝗘 𝗞𝗜𝗗 𝗕𝗛𝗢𝗞 𝗠𝗔𝗧 𝗝𝗬𝗔𝗗𝗔 𝗪𝗔𝗥𝗡𝗔 𝗔𝗡𝗗𝗔𝗥 𝗦𝗘 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗞𝗛𝗢𝗞𝗟𝗔 𝗔𝗨𝗥 𝗔𝗕 𝗞𝗨𝗖𝗛 𝗕𝗢𝗟𝗔 𝗧𝗢𝗛 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂🍆🍑😜👻",
    "𝗧𝗘𝗥𝗜𝗜 𝗠𝗔 𝗠𝗘𝗥𝗘 𝗞𝗔𝗕𝗝𝗘 𝗠𝗔𝗜 𝗛𝗔𝗜 𝗟𝗘𝗡𝗔 𝗠𝗔𝗡 𝗛𝗔𝗜 𝗧𝗢𝗛 𝗣𝗔𝗬 10000000 🤣🤣🤣",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗠𝗢𝗔𝗡 𝗣𝗘 𝗕𝗛𝗜 𝗛𝗜𝗟𝗔 𝗟𝗘𝗧𝗔 𝗛𝗨 𝗜𝗧𝗡𝗜 𝗛𝗢𝗧 𝗛𝗔𝗜 𝗩𝗢𝗛🙈😂👻🍆",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜𝗧𝗡𝗜 𝗛𝗢𝗧 𝗛𝗔𝗜 𝗬𝗔𝗔𝗥 𝗠𝗔𝗡 𝗞𝗥𝗧𝗔 𝗛𝗔𝗜 𝗜𝗧𝗡𝗔 𝗖𝗛𝗢𝗗𝗨 𝗞𝗜 𝗔𝗨𝗥 𝗞𝗢𝗜 𝗖𝗛𝗢𝗗 𝗡𝗔 𝗣𝗔𝗬𝗘 𝗨𝗦𝗞𝗢😂🍑🍆👻",
    "𝗧𝗔𝗔𝗥𝗔𝗞 𝗠𝗘𝗛𝗧𝗔 𝗞𝗔 𝗨𝗟𝗧𝗔 𝗖𝗛𝗔𝗦𝗠𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗔𝗗𝗔 𝗕𝗔𝗗𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂👻🍑🍆",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗣𝗧𝗔𝗞 𝗞𝗘 𝗫𝗛𝗢𝗗 𝗗𝗘𝗡𝗚𝗘 𝗞𝗜 𝗣𝗔𝗧𝗔 𝗩 𝗡𝗛𝗜 𝗖𝗛𝗔𝗟𝗘𝗚𝗔 𝗔𝗨𝗥 𝗕𝗔𝗫𝗫𝗛𝗔 𝗣𝗔𝗜𝗗𝗔 𝗞𝗥 𝗗𝗘𝗚𝗜 🤣🤤🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗢𝗬𝗢 𝗟𝗘 𝗝𝗔𝗔𝗞𝗥 𝗣𝗘𝗟𝗨𝗡𝗚𝗔 𝗜𝗧𝗡𝗔 𝗞𝗜 𝗞𝗔𝗕𝗛𝗜 𝗖𝗛𝗨𝗧 𝗡𝗔𝗛𝗜 𝗗𝗜𝗞𝗛𝗔 𝗣𝗔𝗬𝗘𝗚𝗜 𝗙𝗜𝗥😂🍆👻🍑💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗔𝗜 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗞𝗔 𝗥𝗘𝗘𝗟 𝗟𝗚𝗔 𝗗𝗨𝗡𝗚𝗔 🤤🙈💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗧𝗜𝗞𝗧𝗢𝗞 𝗞𝗜 𝗦𝗔𝗦𝗧𝗜 𝗥𝗔𝗡𝗗𝗜 𝗛𝗔𝗜😂🍆💋",
    "𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗕𝗛𝗢𝗦𝗔𝗗𝗔 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗔𝗠𝗔𝗭𝗢𝗡 𝗠𝗔𝗜 𝗦𝗘𝗟𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 1 𝗠𝗔𝗜 🥺🤣💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗗𝗨𝗕𝗔𝗜 𝗠𝗔𝗜 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔 𝗔𝗨𝗥 𝗫𝗛𝗨𝗗𝗪𝗔 𝗗𝗨𝗡𝗚𝗔 𝗨𝗦𝗞𝗔 𝗣𝗥𝗜𝗡𝗖𝗘 𝗦𝗘 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗩𝗜𝗟𝗟𝗔 𝗟𝗘 𝗝𝗔𝗔𝗞𝗥 𝗣𝗘𝗟𝗨𝗡𝗚𝗔 😂🍆💋🍑",
    "𝗜 𝗙𝗨𝗖𝗞𝗘𝗗 𝗨𝗥 𝗠𝗢𝗠 😂🍆",
    "𝗬𝗢𝗨𝗥 𝗠𝗢𝗧𝗛𝗘𝗥 𝗪𝗜𝗟𝗟 𝗦𝗨𝗖𝗞 𝗠𝗬 𝗗𝗜𝗖𝗞😂🍆🍑",
    "𝗬𝗢𝗨𝗥 𝗠𝗢𝗧𝗛𝗘𝗥 𝗔𝗡𝗗 𝗦𝗜𝗦𝗧𝗘𝗥 𝗜𝗦 𝗩𝗘𝗥𝗬 𝗛𝗢𝗧𝗧 𝗠𝗔𝗡 𝗦𝗛𝗘 𝗦𝗨𝗖𝗞'𝗦 𝗠𝗬 𝗗𝗜𝗖𝗞 𝗘𝗩𝗘𝗥𝗬𝗗𝗔𝗬🙈🍆💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗫𝗫 𝗩𝗜𝗥𝗔𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗕𝗔𝗫𝗖𝗛𝗘 🥵💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗨𝗗𝗞𝗘 𝗗𝗔𝗥 𝗚𝗔𝗬𝗜 𝗬𝗔𝗔𝗥💦👻🙈",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗔 𝗠𝗜𝗗𝗗𝗟𝗘 𝗙𝗜𝗡𝗚𝗘𝗥 𝗡𝗔𝗜𝗟 𝗡𝗔𝗛𝗜 𝗛𝗔𝗜😂👻🍑🍆💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔 𝗫𝗛𝗨𝗗𝗔𝗜 𝗔𝗟𝗜𝗩𝗘 𝗣𝗜𝗖 𝗗𝗔𝗔𝗟 𝗗𝗨𝗡𝗚𝗔 🤤😂",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗖𝗛𝗢𝗗𝗧𝗘 𝗪𝗔𝗞𝗧 𝗬𝗢𝗨𝗧𝗨𝗕𝗘 𝗣𝗘 𝗟𝗜𝗩𝗘 𝗞𝗔𝗥𝗨𝗡𝗚𝗔😂🍆🍑💦",
    "𝗔𝗕𝗜 𝗩 𝗧𝗜𝗠𝗘 𝗛 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗔𝗨𝗥 𝗟𝗨𝗡𝗗 𝗣𝗞𝗔𝗗 🤣🥵💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘 𝗫𝗛𝗨𝗧  𝗠𝗔𝗜 𝗥𝗢𝗖𝗞𝗘𝗧 𝗟𝗔𝗨𝗡𝗖𝗛 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗡𝗔𝗦𝗔 𝗪𝗔𝗟𝗔 🤤💋😱",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗚𝗔𝗥𝗔𝗠 𝗚𝗔𝗥𝗔𝗠 𝗧𝗘𝗟 🥺🤣💋",
    "𝗧𝗘𝗥𝗘 𝗕𝗔𝗔𝗣 𝗔𝗔𝗚𝗬𝗘 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 𝗞𝗔𝗟𝗔𝗣 𝗠𝗧 𝗔𝗕 🤣🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗘𝗞 𝗔𝗨𝗥 𝗫𝗛𝗨𝗧 𝗗𝗔𝗟𝗪𝗔 𝗗𝗨𝗡𝗚𝗔 𝗥𝗡𝗗𝗜 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗣𝗘 𝗖𝗥𝗜𝗖𝗞𝗘𝗧 𝗞𝗛𝗘𝗟𝗡𝗚𝗘 🤣😱",
    "𝗨𝗙𝗙 𝗖𝗛𝗨𝗗 𝗚𝗔𝗬𝗔 𝗕𝗘𝗧𝗔 𝗔𝗕 𝗕𝗛𝗢𝗞 𝗖𝗛𝗨𝗧𝗜𝗬𝗔 𝗕𝗔𝗔𝗣 𝗦𝗘 𝗟𝗔𝗗𝗡𝗘 𝗔𝗔𝗬𝗔 𝗧𝗛𝗔 𝗡𝗔😂🍆🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗣𝗨𝗦𝗦𝗬 𝗖𝗛𝗔𝗧𝗨𝗡𝗚𝗔 𝗕𝗘𝗧𝗘😂🍑🍆🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗛𝗔𝗡𝗘 𝗞𝗜 𝗠𝗔𝗡𝗔𝗚𝗘𝗥 🤤💋",
    "𝗞𝗬𝗔 𝗠𝗧𝗟𝗕 𝗞𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗟𝗢 𝗣𝗔𝗥 𝗣𝗔𝗜𝗦𝗘 𝗗𝗘𝗧𝗘 𝗝𝗔𝗔𝗡𝗔 🤣🔥🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗞𝗜 𝗙𝗔𝗡 𝗛𝗔𝗜😍👻💋🍆",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗞𝗘 𝗧𝗘𝗥𝗘 𝗕𝗔𝗔𝗣 𝗞𝗔𝗔𝗔 𝗟𝗨𝗡𝗗 𝗞𝗔𝗔𝗧 𝗗𝗨𝗡𝗚𝗔 🤣🔥",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗕 𝗣𝗔𝗣𝗔 𝗚𝗔𝗟𝗧𝗜 𝗛𝗢 𝗚𝗔𝗬𝗜 𝗠𝗔𝗔𝗙 𝗞𝗔𝗥𝗗𝗢😁🍑🍆👻",
    "𝗔𝗣𝗡𝗜 𝗠𝗔𝗔 𝗞𝗔𝗔𝗔 𝗚𝗔𝗔𝗔𝗡𝗗 𝗗𝗘𝗗𝗢 🥺 𝗧𝗛𝗢𝗗𝗜 𝗗𝗘𝗥 𝗣𝗘𝗟 𝗞𝗘 𝗗𝗘𝗧𝗔 𝗛𝗨 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗚𝗛𝗔𝗥 𝗕𝗡𝗔 𝗗𝗨𝗡𝗚𝗔 𝗟𝗢𝗗𝗘 🤤💋",
]

que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.4)
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RAIDHU)),
            reply_to=event.message.id,
        )

@bot.on(admin_cmd(pattern="replyraid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="replyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on(admin_cmd(pattern="dreplyraid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="dreplyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")

# mantion added by @Shinchan7222 
# modified By @D3_krish
# bina credit ke Diract gban dunga gand pe😌


@bot.on(admin_cmd(pattern="uraid (.*)"))
@bot.on(sudo_cmd(pattern="uraid (.*)", allow_sudo=True))
async def spam(e):
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(parse_mode=None, link_preview=None )
        predator = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(predator) == 2:
            message = str(predator[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(predator[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(predator[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply( parse_mode=None, link_preview=None )
        
        
        
RAID = [
      "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧 𝗦𝗕𝗦𝗘𝗘𝗘𝗘𝗘 𝗦𝗘𝗘𝗫𝗫𝗫𝗬𝗬𝗬𝗬𝗬 😘💋",
    "𝗧𝗘𝗜𝗥𝗥𝗥𝗥 𝗠𝗔𝗔𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔𝗔𝗔 𝗥𝗔𝗣𝗘𝗘𝗘𝗘𝗘𝗘 𝗞𝗥𝗞𝗘𝗘𝗘𝗘 𝗕𝗛𝗔𝗚𝗚𝗚𝗚𝗚𝗚 𝗝𝗔𝗔𝗔𝗔𝗨𝗡𝗚𝗔𝗔𝗔 👅🤣🤣",
    "𝗧𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔𝗔 𝗣𝗢𝗥𝗡 𝗛𝗨𝗕 𝗠𝗔𝗜𝗜 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗙𝗔𝗔𝗗𝗡𝗘 𝗔𝗔𝗚𝗬𝗘 𝗛𝗔𝗜 𝗕𝗘𝗧𝗜𝗖𝗛𝗢𝗗⚡️⚡️⚡️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗙𝗔𝗧𝗘𝗚𝗜 𝗞𝗜𝗨𝗞𝗜 𝗦𝗕𝗦𝗘 𝗙𝗔𝗦𝗧𝗘𝗦𝗧 𝗕𝗢𝗧 𝗔𝗔𝗚𝗔𝗬𝗔 𝗛𝗔𝗜 𝗧𝗚 𝗣𝗘😈😈⚡️",
    "𝗧𝗥𝗜𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗟𝗘𝗞𝗥 𝗕𝗛𝗔𝗚 𝗝𝗔𝗔𝗨𝗡𝗚𝗔 🤣💋𝗔𝗨𝗥 𝗫𝗫𝗫 𝗕𝗔𝗡𝗔𝗨𝗡𝗚𝗔 🤤",
    "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗜𝗧𝗡𝗔 𝗫𝗛𝗢𝗗𝗨𝗡𝗚𝗔 𝗞𝗜 𝗫𝗛𝗢𝗗𝗧𝗘 𝗫𝗛𝗢𝗗𝗧𝗘 𝗕𝗔𝗫𝗫𝗛𝗘 𝗣𝗔𝗜𝗗𝗔 𝗛𝗢 𝗝𝗔𝗔𝗬𝗘𝗡𝗚𝗘 🤣🔥",
    "𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗨𝗗𝗘𝗚𝗜 𝗕𝗘𝗧𝗘 𝗖𝗛𝗨𝗗 𝗝𝗔𝗬𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧 𝗙𝗔𝗧𝗘𝗚𝗜 𝗔𝗕💦💦🍆🍑😂",
    "𝗧𝗥𝗜𝗜 𝗕𝗔𝗔𝗔𝗣 𝗫𝗛𝗔𝗞𝗞𝗔 𝗛 𝗞𝗬𝗔 ??",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗢𝗗𝗞𝗘 𝗙𝗔𝗥𝗔𝗔𝗥 𝗛𝗢 𝗚𝗔𝗬𝗜😘😂😂😂",
    "𝗧𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗜𝗧𝗡𝗔 𝗫𝗛𝗢𝗗𝗨𝗡𝗚𝗔 𝗞𝗜 𝗫𝗛𝗨𝗧 𝗙𝗔𝗧 𝗝𝗔𝗔𝗬𝗘𝗚𝗜𝗜 🤤🤣🔥",
    "𝗔𝗣𝗡𝗜𝗜𝗜𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢𝗢 𝗣𝗔𝗜𝗗 𝗚𝗜𝗥𝗟𝗟𝗟 𝗕𝗡𝗔 𝗗𝗘𝗘𝗘𝗘 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗘 𝗚𝗨𝗕𝗕𝗔𝗥𝗘 𝗣𝗛𝗘𝗞 𝗞𝗘 𝗠𝗦𝗥𝗨𝗡𝗚𝗔 𝗧𝗨𝗝𝗛𝗘😂🤤💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗠𝗔𝗜 𝗦𝗔𝗥𝗜𝗬𝗔𝗟 𝗗𝗔𝗔𝗟 𝗞𝗘 𝗖𝗛𝗨𝗧 𝗦𝗘 𝗕𝗔𝗛𝗔𝗥 𝗡𝗜𝗞𝗔𝗟𝗨𝗡𝗚𝗔 💦🍆🍑😈",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗚𝗕 𝗥𝗢𝗔𝗗 𝗞𝗜 𝗦𝗔𝗦𝗧𝗜 𝗥𝗔𝗡𝗗𝗜 𝗛𝗔𝗜 𝗕𝗘𝗧𝗘😂💋🍑🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗕𝗣 𝗦𝗛𝗢𝗢𝗧 𝗞𝗔𝗥𝗞𝗘 𝗣𝗢𝗥𝗡𝗛𝗨𝗕 𝗣𝗘 𝗗𝗔𝗟𝗨𝗡𝗚𝗔 😝🍑😂🔥",
    "𝗔𝗔𝗝 𝗧𝗘𝗥𝗔 𝗞𝗛𝗔𝗡𝗗𝗔𝗡 𝗫𝗛𝗨𝗗𝗘𝗚𝗔 💦🍆🍑",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗣𝗘 𝗝𝗛𝗨𝗟𝗘𝗚𝗜🍆🍑😁",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗞𝗢 𝗗𝗔𝗗𝗗𝗬 𝗕𝗢𝗟𝗧𝗜 𝗛𝗔𝗜😂🤤🍑💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔 𝗚𝗔𝗡𝗚 𝗕𝗔𝗡𝗚 𝗞𝗥𝗔 𝗗𝗨𝗡𝗚𝗔 🤣🔥💋 ",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗨𝗦𝗜 𝗞𝗜 𝗫𝗛𝗨𝗧 𝗞𝗔𝗔𝗟𝗜 𝗔𝗬𝗘 𝗛𝗔𝗜 𝗧𝗘𝗥𝗜 𝗧𝗢𝗛 𝗛𝗨𝗠𝗡𝗘 𝗚𝗔𝗔𝗡𝗗 𝗙𝗔𝗔𝗗 𝗗𝗔𝗔𝗟𝗜💦🍆🍑🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗖𝗔𝗥 𝗟𝗔𝗚𝗔 𝗗𝗨𝗡𝗚𝗔 𝗞𝗜𝗗𝗗 🤣🔥",
    "𝗧𝗘𝗥𝗔 𝗕𝗔𝗔𝗣 𝗞𝗢 𝗠𝗔𝗔𝗔𝗥 𝗗𝗨𝗡𝗚𝗔𝗔𝗔𝗔 𝗕𝗔𝗫𝗫𝗛𝗘 🤣👅 ",
    "𝗧𝗘𝗥𝗜 𝗚𝗔𝗔𝗡𝗗 𝗙𝗧 𝗟𝗘 𝗧𝗨𝗞𝗗𝗘 𝗛𝗢 𝗚𝗔𝗬𝗘 𝗖𝗛𝗔𝗔𝗥 𝗔𝗕𝗘 𝗖𝗛𝗔𝗟 𝗡𝗜𝗞𝗔𝗟 𝗪𝗔𝗥𝗡𝗔 𝗜𝗧𝗡𝗔 𝗠𝗔𝗥𝗨𝗡𝗚𝗔 𝗞𝗜 𝗛𝗢 𝗝𝗔𝗜𝗘𝗚𝗔 𝗧𝗘𝗥𝗔 𝗛𝗔𝗔𝗟 𝗕𝗘𝗛𝗔𝗟😂😎😈⚡️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔𝗔𝗔 𝗠𝗘𝗥𝗞𝗢 𝗗𝗔𝗗𝗗𝗬 𝗡𝗔𝗔𝗠 𝗦𝗘 𝗣𝗨𝗞𝗔𝗥𝗘𝗘𝗘😌😂😈🍑",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗦𝗕𝗦𝗘 𝗔𝗖𝗖𝗛𝗜 𝗣𝗔𝗜𝗗 𝗚𝗜𝗥𝗟 🤤💋",
    "𝗔𝗕𝗘 𝗔𝗔𝗝 𝗧𝗘𝗥𝗜 𝗚𝗔𝗔𝗡𝗗𝗔𝗜 𝗟𝗘𝗗 𝗙𝗜𝗧 𝗞𝗔𝗥𝗨𝗡𝗚𝗔 𝗙𝗜𝗥 𝗧𝗘𝗥𝗜 𝗧𝗔𝗔𝗡𝗗 𝗖𝗛𝗔𝗠𝗔𝗞 𝗨𝗧𝗛𝗘𝗚𝗜😂🍆🍑",
    "𝗧𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗦𝗔𝗦𝗧𝗔 𝗦𝗣𝗔𝗠🤣 𝗕𝗢𝗧 𝗟𝗔𝗚𝗔 𝗞𝗘 𝗦𝗣𝗔𝗠 𝗞𝗥𝗨𝗡𝗚𝗔 🤤💋",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗔𝗨𝗗𝗘 𝗣𝗘 𝗙𝗜𝗦𝗔𝗟 𝗞𝗔𝗥 𝗚𝗜𝗥 𝗚𝗔𝗬𝗜 𝗔𝗨𝗥 𝗣𝗥𝗘𝗚𝗡𝗔𝗡𝗧 𝗛𝗢 𝗚𝗔𝗬𝗜😂🍑🍆💋",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗡𝗘 𝗠𝗘𝗥𝗔 𝗡𝗨𝗠𝗕𝗘𝗥 𝗗𝗔𝗗𝗗𝗬 𝗡𝗔𝗠𝗘 𝗦𝗘 𝗦𝗔𝗩𝗘 𝗞𝗔𝗥 𝗥𝗞𝗛𝗔 𝗛𝗔𝗜🙈👻😈💋",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗢 𝗟𝗔𝗨𝗗𝗘 𝗣𝗘 𝗡𝗔𝗖𝗛𝗔𝗨𝗡𝗚𝗔 😂🍆🍑",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗞𝗜 𝗗𝗜𝗘 𝗛𝗔𝗥𝗗 𝗙𝗔𝗡 𝗛𝗔𝗜 👻🙈😂💋",
    "𝗞𝗬𝗔 𝗠𝗧𝗟𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗦𝗘 𝗣𝗘𝗛𝗟𝗘 3 𝗗𝗜𝗟𝗗𝗢 𝗔𝗨𝗥 𝗘𝗞 𝗩𝗜𝗕𝗥𝗔𝗧𝗢𝗥 𝗨𝗦𝗘 𝗞𝗔𝗥𝗧𝗜 𝗧𝗛𝗜😂🍑👻🍆💦",
    "𝗔𝗣𝗡𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗫𝗛𝗨𝗧 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗭𝗢𝗠𝗔𝗧𝗢 𝗠𝗔𝗜 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔 💋🤤🥵",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗔 𝗣𝗔𝗣𝗔 𝗞𝗔 𝗟𝗨𝗡𝗗 𝗠𝗔𝗜 𝗗𝗨𝗠 𝗡𝗔𝗛𝗜 𝗧𝗛𝗔 𝗜𝗦𝗟𝗜𝗬𝗘 𝗠𝗘𝗥𝗘 𝗦𝗘 𝗖𝗛𝗨𝗗𝗞𝗘 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗡𝗘 𝗧𝗨𝗝𝗛𝗘 𝗝𝗔𝗡𝗔𝗠 𝗗𝗜𝗬𝗔🍆💦🍑😂👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗔𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗔𝗠𝗔𝗭𝗢𝗡 𝗠𝗔𝗜 𝗦𝗘𝗟𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 50 𝗠𝗔𝗜 🤤💋😊❤️",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗢 𝗖𝗛𝗢𝗖𝗢𝗟𝗔𝗧𝗘 𝗙𝗟𝗔𝗩𝗢𝗨𝗥 𝗣𝗔𝗦𝗔𝗡𝗗 𝗛𝗔𝗜👻🍆🍑😂",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗘 𝗚𝗛𝗔𝗥 𝗞𝗘 𝗣𝗔𝗔𝗦 𝗪𝗔𝗟𝗘 𝗗𝗨𝗞𝗔𝗡 𝗠𝗔𝗜 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 200 𝗞𝗘 𝗕𝗛𝗔𝗩 𝗕𝗜𝗞 𝗥𝗛𝗜 𝗛𝗔𝗜😂👻🍆🍑",
    "𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗫𝗛𝗨𝗧 𝗦𝗕𝗦𝗘 𝗦𝗘𝗫𝗫𝗬 𝗛 𝗠𝗔𝗗𝗔𝗥𝗫𝗝𝗢𝗗 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗙𝗔𝗧 𝗞𝗘 𝗛𝗢 𝗚𝗔𝗬𝗘 𝗧𝗨𝗞𝗗𝗘 𝗖𝗛𝗔𝗔𝗥😂🍑🍆👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧𝗧𝗧 𝗙𝗔𝗔𝗔𝗗 𝗞𝗘 𝗦𝗔𝗕 𝗦𝗘 𝗖𝗛𝗨𝗗𝗪𝗔𝗡𝗨𝗡𝗚𝗔 🤤💋🔥",
    "𝗔𝗡𝗗𝗜 𝗠𝗔𝗡𝗗𝗜 𝗦𝗔𝗡𝗗𝗜 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗫𝗛𝗨𝗧𝗧𝗧😂👻🍆🍑",
    "𝗔𝗔𝗨𝗞𝗔𝗔𝗧 𝗠𝗔𝗜 𝗥𝗘𝗛 𝗞𝗔𝗥 𝗕𝗔𝗔𝗧 𝗞𝗥 𝗟𝗜𝗬𝗔 𝗞𝗥 𝗕𝗔𝗫𝗫𝗛𝗘 𝗪𝗔𝗥𝗡𝗔 𝗠𝗔𝗔𝗔 𝗫𝗛𝗢𝗗 𝗗𝗘𝗡𝗚𝗘 🤣🔥🖕",
    "𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗔 𝗟𝗨𝗡𝗗 𝗗𝗘𝗞𝗛𝗞𝗥 𝗗𝗔𝗘 𝗚𝗔𝗬𝗜 𝗗𝗔𝗥𝗞𝗘 𝗨𝗦𝗡𝗘 𝗗𝗜𝗬𝗔 𝗠𝗨𝗧 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗞𝗔𝗔𝗟𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧😂🍑👻",
    "𝗛𝗔𝗥𝗘 𝗛𝗔𝗥𝗘 𝗝𝗛𝗔𝗗𝗜𝗬𝗢 𝗠𝗘 𝗕𝗔𝗗𝗔 𝗕𝗔𝗗𝗔 𝗚𝗛𝗢𝗦𝗟𝗔 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂🍑🍆👻",
    "𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗔 𝗟𝗨𝗡𝗗 𝗗𝗘𝗞𝗛𝗞𝗥 𝗗𝗔𝗘 𝗚𝗔𝗬𝗜 𝗗𝗔𝗥𝗞𝗘 𝗨𝗦𝗡𝗘 𝗗𝗜𝗬𝗔 𝗠𝗨𝗧 𝗔𝗥𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗞𝗔𝗔𝗟𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧𝗧𝗧𝗧𝗧😂🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗟𝗘𝗞𝗘 𝗕𝗛𝗔𝗚 𝗝𝗔𝗔𝗨𝗡𝗚𝗔  🤤💋𝗔𝗨𝗥 𝗞𝗔𝗟 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔  𝗗𝗜𝗞𝗛𝗘𝗚𝗜 𝗖𝗜𝗗 𝗠𝗔𝗜 🤣🔥",
    "𝗔𝗥𝗘 𝗕𝗘𝗧𝗘 CUTE KING 𝗞𝗘 𝗣𝗜𝗥𝗢 𝗕𝗢𝗧 𝗦𝗘 𝗖𝗛𝗨𝗗 𝗚𝗔𝗬𝗔 𝗧𝗨 𝗡𝗜𝗞𝗟 𝗪𝗔𝗥𝗡𝗔 𝗔𝗨𝗥 𝗖𝗛𝗨𝗗𝗘𝗚𝗔 𝗕𝗘𝗧𝗘😁🍆🔥🍑",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗞𝗜 𝗞𝗔𝗔𝗟𝗜 𝗫𝗛𝗨𝗧 𝗟𝗘𝗔𝗞 𝗞𝗔𝗥 𝗥𝗛𝗜 𝗛𝗔𝗜 𝗠𝗔𝗜 𝗣𝗟𝗨𝗠𝗕𝗘𝗥 𝗛𝗨 𝗥𝗨𝗞 𝗧𝗛𝗜𝗞 𝗞𝗔𝗥 𝗗𝗨𝗡𝗚𝗔😂🍆🍑👻",
    "𝗔𝗡𝗗𝗜𝗜 𝗠𝗔𝗡𝗗𝗜𝗜𝗜 𝗦𝗛𝗔𝗡𝗗𝗜𝗜𝗜 𝗔𝗚𝗔𝗥 𝗗𝗨𝗦𝗠𝗔𝗡 𝗟𝗢𝗚 𝗥𝗘𝗣𝗟𝗬 𝗞𝗜𝗬𝗔 𝗧𝗢𝗛 𝗨𝗦𝗞𝗔 𝗠𝗔 𝗕𝗛𝗘𝗡 𝗥𝗔𝗡𝗗𝗜𝗜 😅😅😒",
    "𝗧𝗨 𝗔𝗨𝗥 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗖𝗔𝗥 𝗖𝗛𝗔𝗗𝗔 𝗗𝗨𝗡𝗚𝗔 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 🤣🔥",
    "𝗔𝗥𝗘 𝗝𝗬𝗔𝗗𝗔 𝗨𝗗 𝗠𝗔𝗧 𝗪𝗔𝗥𝗡𝗔 𝗣𝗛𝗢𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗔 𝗞𝗛𝗢𝗣𝗗𝗔 𝗔𝗨𝗥 𝗝𝗬𝗔𝗗𝗔 𝗕𝗢𝗟𝗘𝗚𝗔 𝗧𝗢𝗛 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗔 𝗕𝗚𝗢𝗦𝗗𝗔😂🍆🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗦𝗔𝗕 𝗞𝗢 𝗕𝗔𝗔𝗧 𝗗𝗨𝗡𝗚𝗔 🤣✌️",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔𝗔 𝗞𝗢 𝗞𝗜𝗗𝗡𝗔𝗣 𝗞𝗥𝗞𝗘 𝗡𝗔𝗡𝗚𝗔 𝗥𝗢𝗔𝗗 𝗣𝗘 𝗫𝗛𝗢𝗗 𝗗𝗨𝗡𝗙𝗔 🤣🤤🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗬𝗬𝗜𝗔 𝗧𝗢𝗛 𝗞𝗔𝗟𝗔𝗣𝗡𝗘 𝗟𝗔𝗚𝗜 🤣🥺",
    "𝗔𝗕𝗘 𝗞𝗜𝗗 𝗕𝗛𝗢𝗞 𝗠𝗔𝗧 𝗝𝗬𝗔𝗗𝗔 𝗪𝗔𝗥𝗡𝗔 𝗔𝗡𝗗𝗔𝗥 𝗦𝗘 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗞𝗛𝗢𝗞𝗟𝗔 𝗔𝗨𝗥 𝗔𝗕 𝗞𝗨𝗖𝗛 𝗕𝗢𝗟𝗔 𝗧𝗢𝗛 𝗙𝗔𝗔𝗗 𝗗𝗨𝗡𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂🍆🍑😜👻",
    "𝗧𝗘𝗥𝗜𝗜 𝗠𝗔 𝗠𝗘𝗥𝗘 𝗞𝗔𝗕𝗝𝗘 𝗠𝗔𝗜 𝗛𝗔𝗜 𝗟𝗘𝗡𝗔 𝗠𝗔𝗡 𝗛𝗔𝗜 𝗧𝗢𝗛 𝗣𝗔𝗬 10000000 🤣🤣🤣",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗠𝗢𝗔𝗡 𝗣𝗘 𝗕𝗛𝗜 𝗛𝗜𝗟𝗔 𝗟𝗘𝗧𝗔 𝗛𝗨 𝗜𝗧𝗡𝗜 𝗛𝗢𝗧 𝗛𝗔𝗜 𝗩𝗢𝗛🙈😂👻🍆",
    "𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜𝗧𝗡𝗜 𝗛𝗢𝗧 𝗛𝗔𝗜 𝗬𝗔𝗔𝗥 𝗠𝗔𝗡 𝗞𝗥𝗧𝗔 𝗛𝗔𝗜 𝗜𝗧𝗡𝗔 𝗖𝗛𝗢𝗗𝗨 𝗞𝗜 𝗔𝗨𝗥 𝗞𝗢𝗜 𝗖𝗛𝗢𝗗 𝗡𝗔 𝗣𝗔𝗬𝗘 𝗨𝗦𝗞𝗢😂🍑🍆👻",
    "𝗧𝗔𝗔𝗥𝗔𝗞 𝗠𝗘𝗛𝗧𝗔 𝗞𝗔 𝗨𝗟𝗧𝗔 𝗖𝗛𝗔𝗦𝗠𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗔𝗗𝗔 𝗕𝗔𝗗𝗔 𝗕𝗛𝗢𝗦𝗗𝗔😂👻🍑🍆",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗣𝗧𝗔𝗞 𝗞𝗘 𝗫𝗛𝗢𝗗 𝗗𝗘𝗡𝗚𝗘 𝗞𝗜 𝗣𝗔𝗧𝗔 𝗩 𝗡𝗛𝗜 𝗖𝗛𝗔𝗟𝗘𝗚𝗔 𝗔𝗨𝗥 𝗕𝗔𝗫𝗫𝗛𝗔 𝗣𝗔𝗜𝗗𝗔 𝗞𝗥 𝗗𝗘𝗚𝗜 🤣🤤🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗢𝗬𝗢 𝗟𝗘 𝗝𝗔𝗔𝗞𝗥 𝗣𝗘𝗟𝗨𝗡𝗚𝗔 𝗜𝗧𝗡𝗔 𝗞𝗜 𝗞𝗔𝗕𝗛𝗜 𝗖𝗛𝗨𝗧 𝗡𝗔𝗛𝗜 𝗗𝗜𝗞𝗛𝗔 𝗣𝗔𝗬𝗘𝗚𝗜 𝗙𝗜𝗥😂🍆👻🍑💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗔𝗜 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 𝗞𝗔 𝗥𝗘𝗘𝗟 𝗟𝗚𝗔 𝗗𝗨𝗡𝗚𝗔 🤤🙈💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗧𝗜𝗞𝗧𝗢𝗞 𝗞𝗜 𝗦𝗔𝗦𝗧𝗜 𝗥𝗔𝗡𝗗𝗜 𝗛𝗔𝗜😂🍆💋",
    "𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗡 𝗞𝗔 𝗕𝗛𝗢𝗦𝗔𝗗𝗔 𝗙𝗔𝗔𝗗 𝗞𝗘 𝗔𝗠𝗔𝗭𝗢𝗡 𝗠𝗔𝗜 𝗦𝗘𝗟𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 1 𝗠𝗔𝗜 🥺🤣💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗗𝗨𝗕𝗔𝗜 𝗠𝗔𝗜 𝗕𝗛𝗘𝗝 𝗗𝗨𝗡𝗚𝗔 𝗔𝗨𝗥 𝗫𝗛𝗨𝗗𝗪𝗔 𝗗𝗨𝗡𝗚𝗔 𝗨𝗦𝗞𝗔 𝗣𝗥𝗜𝗡𝗖𝗘 𝗦𝗘 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗩𝗜𝗟𝗟𝗔 𝗟𝗘 𝗝𝗔𝗔𝗞𝗥 𝗣𝗘𝗟𝗨𝗡𝗚𝗔 😂🍆💋🍑",
    "𝗜 𝗙𝗨𝗖𝗞𝗘𝗗 𝗨𝗥 𝗠𝗢𝗠 😂🍆",
    "𝗬𝗢𝗨𝗥 𝗠𝗢𝗧𝗛𝗘𝗥 𝗪𝗜𝗟𝗟 𝗦𝗨𝗖𝗞 𝗠𝗬 𝗗𝗜𝗖𝗞😂🍆🍑",
    "𝗬𝗢𝗨𝗥 𝗠𝗢𝗧𝗛𝗘𝗥 𝗔𝗡𝗗 𝗦𝗜𝗦𝗧𝗘𝗥 𝗜𝗦 𝗩𝗘𝗥𝗬 𝗛𝗢𝗧𝗧 𝗠𝗔𝗡 𝗦𝗛𝗘 𝗦𝗨𝗖𝗞'𝗦 𝗠𝗬 𝗗𝗜𝗖𝗞 𝗘𝗩𝗘𝗥𝗬𝗗𝗔𝗬🙈🍆💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗫𝗫 𝗩𝗜𝗥𝗔𝗟 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗕𝗔𝗫𝗖𝗛𝗘 🥵💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗜𝗬𝗔 𝗖𝗛𝗨𝗗𝗞𝗘 𝗗𝗔𝗥 𝗚𝗔𝗬𝗜 𝗬𝗔𝗔𝗥💦👻🙈",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗔𝗕 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗔 𝗠𝗜𝗗𝗗𝗟𝗘 𝗙𝗜𝗡𝗚𝗘𝗥 𝗡𝗔𝗜𝗟 𝗡𝗔𝗛𝗜 𝗛𝗔𝗜😂👻🍑🍆💦",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔 𝗫𝗛𝗨𝗗𝗔𝗜 𝗔𝗟𝗜𝗩𝗘 𝗣𝗜𝗖 𝗗𝗔𝗔𝗟 𝗗𝗨𝗡𝗚𝗔 🤤😂",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗖𝗛𝗢𝗗𝗧𝗘 𝗪𝗔𝗞𝗧 𝗬𝗢𝗨𝗧𝗨𝗕𝗘 𝗣𝗘 𝗟𝗜𝗩𝗘 𝗞𝗔𝗥𝗨𝗡𝗚𝗔😂🍆🍑💦",
    "𝗔𝗕𝗜 𝗩 𝗧𝗜𝗠𝗘 𝗛 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗔𝗨𝗥 𝗟𝗨𝗡𝗗 𝗣𝗞𝗔𝗗 🤣🥵💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘𝗘 𝗫𝗛𝗨𝗧  𝗠𝗔𝗜 𝗥𝗢𝗖𝗞𝗘𝗧 𝗟𝗔𝗨𝗡𝗖𝗛 𝗞𝗥 𝗗𝗨𝗡𝗚𝗔 𝗡𝗔𝗦𝗔 𝗪𝗔𝗟𝗔 🤤💋😱",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗚𝗔𝗥𝗔𝗠 𝗚𝗔𝗥𝗔𝗠 𝗧𝗘𝗟 🥺🤣💋",
    "𝗧𝗘𝗥𝗘 𝗕𝗔𝗔𝗣 𝗔𝗔𝗚𝗬𝗘 𝗠𝗔𝗗𝗔𝗥𝗫𝗛𝗢𝗗 𝗞𝗔𝗟𝗔𝗣 𝗠𝗧 𝗔𝗕 🤣🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗔𝗔𝗔 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗘𝗞 𝗔𝗨𝗥 𝗫𝗛𝗨𝗧 𝗗𝗔𝗟𝗪𝗔 𝗗𝗨𝗡𝗚𝗔 𝗥𝗡𝗗𝗜 🤤💋🔥",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗣𝗘 𝗖𝗥𝗜𝗖𝗞𝗘𝗧 𝗞𝗛𝗘𝗟𝗡𝗚𝗘 🤣😱",
    "𝗨𝗙𝗙 𝗖𝗛𝗨𝗗 𝗚𝗔𝗬𝗔 𝗕𝗘𝗧𝗔 𝗔𝗕 𝗕𝗛𝗢𝗞 𝗖𝗛𝗨𝗧𝗜𝗬𝗔 𝗕𝗔𝗔𝗣 𝗦𝗘 𝗟𝗔𝗗𝗡𝗘 𝗔𝗔𝗬𝗔 𝗧𝗛𝗔 𝗡𝗔😂🍆🍑👻",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗣𝗨𝗦𝗦𝗬 𝗖𝗛𝗔𝗧𝗨𝗡𝗚𝗔 𝗕𝗘𝗧𝗘😂🍑🍆🤤",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗛𝗔𝗡𝗘 𝗞𝗜 𝗠𝗔𝗡𝗔𝗚𝗘𝗥 🤤💋",
    "𝗞𝗬𝗔 𝗠𝗧𝗟𝗕 𝗞𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗟𝗢 𝗣𝗔𝗥 𝗣𝗔𝗜𝗦𝗘 𝗗𝗘𝗧𝗘 𝗝𝗔𝗔𝗡𝗔 🤣🔥🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗠𝗘𝗥𝗘 𝗟𝗢𝗗𝗘 𝗞𝗜 𝗙𝗔𝗡 𝗛𝗔𝗜😍👻💋🍆",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗞𝗘 𝗧𝗘𝗥𝗘 𝗕𝗔𝗔𝗣 𝗞𝗔𝗔𝗔 𝗟𝗨𝗡𝗗 𝗞𝗔𝗔𝗧 𝗗𝗨𝗡𝗚𝗔 🤣🔥",
    "𝗞𝗬𝗔 𝗠𝗔𝗧𝗟𝗕 𝗣𝗔𝗣𝗔 𝗚𝗔𝗟𝗧𝗜 𝗛𝗢 𝗚𝗔𝗬𝗜 𝗠𝗔𝗔𝗙 𝗞𝗔𝗥𝗗𝗢😁🍑🍆👻",
    "𝗔𝗣𝗡𝗜 𝗠𝗔𝗔 𝗞𝗔𝗔𝗔 𝗚𝗔𝗔𝗔𝗡𝗗 𝗗𝗘𝗗𝗢 🥺 𝗧𝗛𝗢𝗗𝗜 𝗗𝗘𝗥 𝗣𝗘𝗟 𝗞𝗘 𝗗𝗘𝗧𝗔 𝗛𝗨 🤤💋",
    "𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗔 𝗞𝗘𝗘 𝗫𝗛𝗨𝗧 𝗠𝗔𝗜 𝗚𝗛𝗔𝗥 𝗕𝗡𝗔 𝗗𝗨𝗡𝗚𝗔 𝗟𝗢𝗗𝗘 🤤💋",
]

CmdHelp("reply_raid").add_command(
  "replyraid", "<reply to user>" 
).add_command(
  "uraid", "<username/reply>" 
).add_command(
  "dreplyraid", "<username/reply>"
).add()
