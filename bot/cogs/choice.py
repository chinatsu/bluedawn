from discord.ext import commands
import random

greetings = ["ey", "eyyyy", "hi"]


class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delimiters = [" or ", " | ", "; ", ", ", ",", ";", "|"]

    def split_choices(self, msg):
        for delimiter in self.delimiters:
            msg = "|".join(msg.split(delimiter))
        return msg.split("|")

    @commands.command(name="choice", aliases=["choose", "decide"])
    async def choose(self, ctx, *, choices):
        """Provided a list of choices, the bot will choose for you.
        The list can be delimited a number of ways:
            a, b or c
            a | b | c
            a, b, c
            a; b; c
        are all equivalent.
        """
        choices = self.split_choices(choices)
        choice = random.choice(choices)
        await ctx.send(f"{self.bot.name} says: {choice}")


def setup(bot):
    bot.add_cog(Choice(bot))
