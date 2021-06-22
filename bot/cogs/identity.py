from discord.ext import commands
import random
from datetime import date
from yaml import load, Loader


def fetch_adjectives():
    with open("bot/cogs/resources/adjectives.yaml") as f:
        adjectives = load(f, Loader=Loader)
    return adjectives


def fetch_nouns():
    with open("bot/cogs/resources/nouns.yaml") as f:
        nouns = load(f, Loader=Loader)
    return nouns


class Identity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.adjectives = fetch_adjectives()
        self.nouns = fetch_nouns()

    def get_seed(self, user_id):
        return date.today().toordinal() + user_id

    def get_identity(self):
        identity = []

        adjectives = []
        for _ in range(random.randint(1, 3)):
            choice = random.choice(self.adjectives)
            if choice in identity:
                choice = random.choice(self.adjectives)
            adjectives.append(choice)
        identity.append(", ".join(adjectives))
        identity.append(random.choice(self.nouns))

        return " ".join(identity)

    @commands.command(name="identity")
    async def identity(self, ctx):
        seed = self.get_seed(ctx.author.id)
        random.seed(seed)
        identity = self.get_identity()
        article = "an" if identity[0] in ["a", "e", "i", "o", "u"] else "a"
        await ctx.send(
            f"{self.bot.name} says: you look like {article} **{identity}** today"
        )


def setup(bot):
    bot.add_cog(Identity(bot))
