from discord.ext import commands
import discord
import random

greetings = ["ey", "eyyyy", "hi"]

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_message(self, ctx):
        user_id = self.bot.user.id
        msg = ctx.message.content
        for prefix in self.bot.command_prefix(self.bot, None):
            if msg.startswith(prefix):
                msg = msg.removeprefix(prefix)
        return msg

    @commands.command(name="hello", aliases=["ey"])
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        message = self.get_message(ctx)
        print(message)
        if message == "hello":
            reply = "hello"
        else:
            reply = random.choice(greetings)
        await ctx.send(f'{reply} {member.name}')

def setup(bot):
    bot.add_cog(Hello(bot))