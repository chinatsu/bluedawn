from discord.ext import commands
import discord
import random

greetings = ["ey", "eyyyy", "hi"]

class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delimiters = [", ", ",", ";", "|"]

    def split_choices(self, msg):
        for delimiter in self.delimiters:
            msg = "|".join(msg.split(delimiter))
        return msg.split("|")

    @commands.command(name="choice", aliases=["choose", "decide"])
    async def choose(self, ctx, *, choices):
        choices = self.split_choices(choices)
        choice = random.choice(choices)
        await ctx.send(f'ganesh says: {choice}')

def setup(bot):
    bot.add_cog(Choice(bot))