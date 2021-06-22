from discord.ext import commands
import discord
from .util import selfinfo, whois


class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gitrev = selfinfo.get_git_revision()
        self.semantic_ver = selfinfo.get_semantic_version()

    @commands.command(name="whois")
    async def whois(self, ctx, *, target: discord.Member = None):
        """Displays info about a member on the server.
        Requesting to view this bot will show the current version and git hash also.
        """
        member = target or ctx.author
        name = member.display_name
        if member.id == self.bot.user.id:
            name = f"{self.bot.user.name} v{self.semantic_ver} ({self.gitrev})"
            member = ctx.guild.get_member(self.bot.user.id)

        embed = whois.embed(member, name)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Whois(bot))
