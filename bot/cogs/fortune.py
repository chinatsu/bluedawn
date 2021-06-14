from discord.ext import commands
import discord
import random
import json
from datetime import date


fortunes = ["v good", "good", "neutral", "bad", "v bad"]

class Fortune(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_seed(self, user_id):
        return date.today().toordinal() + user_id
        
    @commands.command(name="fortune", aliases=["f"])
    async def fortune(self, ctx):
        member = ctx.author
        seed = self.get_seed(member.id)
        random.seed(seed)
        fortune = random.choice(fortunes)
        await ctx.send(f'ganesh says your fortune today is **{fortune}**')

def setup(bot):
    bot.add_cog(Fortune(bot))