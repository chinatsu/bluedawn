from discord.ext import commands
import discord.utils


def is_owner():
    def is_owner_check(ctx):
        return ctx.message.author.id == 125307006260084736

    return commands.check(is_owner_check)
