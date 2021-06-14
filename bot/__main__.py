import discord
from discord.ext import commands
import traceback
import sys
from secret import TOKEN

description = """
    I am a bot!
    """

initial_extensions = [
    'cogs.hello',
    'cogs.choice',
    'cogs.fortune',
]

def _prefix_callable(bot, msg):
    user_id = bot.user.id
    return [f'<@!{user_id}> ', f'<@{user_id}> ', '!']

class Bluedawn(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_prefix_callable, description=description)
        for ext in initial_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f'Failed to load extension {ext}.', file=sys.stderr)
                traceback.print_exc()

    async def on_ready(self):
        print(f"Logged on as {self.user}")



client = Bluedawn()
client.run(TOKEN)