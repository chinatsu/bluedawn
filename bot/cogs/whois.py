from discord.ext import commands
import discord
import subprocess
from .util import selfinfo
from datetime import datetime


def format_date(d):
    return d.strftime("%a %d. %B %Y, %H:%M UTC")

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gitrev = selfinfo.get_git_revision()
        self.semantic_ver = selfinfo.get_semantic_version()

    def whoisembed(self, user, name):
        e = discord.Embed(title=name, colour=user.colour)
        e.set_footer(text=f"{user.name}#{user.discriminator} ({user.id})")
        e.set_image(url=user.avatar_url)
        e.add_field(name="Status", value=user.status, inline=True)
        e.add_field(name="Registered", value=format_date(user.created_at), inline=True)
        e.add_field(name="Joined", value=format_date(user.joined_at), inline=True)
        if user.bot:
            e.description = "Bot"
        if user.premium_since:
            e.add_field(name="Boosted server", value=format_date(user.premium_since), inline=True)
        for activity in user.activities:
            if activity.type == discord.ActivityType.listening:
                e.add_field(name="Listening to", value=f"[{activity.artist} - {activity.title}](https://open.spotify.com/track/{activity.track_id})", inline=True)
            if activity.type == discord.ActivityType.playing:
                e.add_field(name="Playing", value=activity.name, inline=True)
            if activity.type == discord.ActivityType.streaming:
                e.add_field(name="Streaming", value=f"[{activity.game} ({activity.name})]({activity.url})", inline=True)
            if activity.type == discord.ActivityType.custom:
                e.add_field(name="Playing?", value=activity.name, inline=True)
        return e

        
    @commands.command(name="whois")
    async def whois(self, ctx, *, target: discord.Member = None):
        member = target or ctx.author
        name = member.display_name
        if member.id == self.bot.user.id:
            name = f"{self.bot.user.name} v{self.semantic_ver} ({self.gitrev})"
            member = ctx.guild.get_member(self.bot.user.id)

        embed = self.whoisembed(member, name)
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Whois(bot))