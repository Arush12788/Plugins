
import asyncio
import random

from . import *

KKK_STR = [
   "ARSH IS BEST",
    "ARSH KO I LOVE YOU BOL DO",
     "ARSH BABY HOT HAI",
   "YOU SHOULD JUST MARRY ARSH",
    " ARSH KI CUTIE AAP BAN JAO ",
]

@Pbx_cmd(pattern="atarifa(?:\s|$)([\s\S]*)")
async def atarif(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).split(" ")
    if len(args) != 2:
        await event.reply("Usage: .raid @username <count>")
        return
    victim = args[0]
    count = args[1]

    if not count.isdigit():
        await event.reply("Count must be a valid number.")
        return

    count = int(count)

    victim_entity = await event.client.get_entity(victim)
    victim_username = f"@{victim_entity.username}" if victim_entity.username else victim_entity.id
    await event.delete()
    for _ in range(count):
        message = f"{victim_username} {random.choice(KKK_STR)}"
        await event.reply(message)

CmdHelp("atarifa").add_command(
    "atarifa", None, "Starts raid on a user by sending insults a specified number of times, each insult in a separate message."
).add()
