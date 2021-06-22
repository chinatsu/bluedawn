from discord.ext import commands
import random


responses = [
    "it is certain",
    "it is decidedly so",
    "without a doubt",
    "yes definitely",
    "you may rely on it",
    "as i see it, yes",
    "most likely",
    "outlook good",
    "yes",
    "signs point to yes",
    "reply hazy, try again",
    "ask again later",
    "better not tell you now",
    "cannot predict now",
    "concentrate and ask again",
    "don't count on it",
    "my reply is no",
    "my sources say no",
    "outlook not so good",
    "very doubtful",
]


class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", aliases=["8"])
    async def fortune(self, ctx):
        response = random.choice(responses)
        await ctx.send(f"{self.bot.name} says: **{response}**")


def setup(bot):
    bot.add_cog(EightBall(bot))
