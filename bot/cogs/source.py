from discord.ext import commands
import aiohttp


class Source(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="source")
    async def fortune(self, ctx, cog=None):
        cogs = [k.lower() for k in self.bot.cogs.keys()]
        if cog is None:
            await ctx.send("https://github.com/chinatsu/bluedawn")
            return
        if cog not in cogs:
            await ctx.send(
                f"`{cog}` is not a recognized module. Must be one of `{cogs}`"
            )
            return
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://raw.githubusercontent.com/chinatsu/bluedawn/main/bot/cogs/{cog}.py"
            ) as resp:
                if resp.status != 200:
                    await ctx.send(
                        f"Tried to fetch source code for {cog}, but got HTTP Status {resp.status}"
                    )
                    return
                text = await resp.text()
        await ctx.send(f"```python\n{text}\n```")


def setup(bot):
    bot.add_cog(Source(bot))
