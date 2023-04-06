from discord.ext import commands
import discord
import aiohttp

watching_query = '''
query ($name: String) { 
    MediaListCollection(userName: $name, status: PLANNING, type: ANIME) {
        lists {
          entries {
                media {
                    status,
                    id,
                    idMal,
                    episodes,
                    title {
                      romaji
                    },
                    nextAiringEpisode {
                      airingAt,
                      episode
                    }
                }
            }
        }
    }
}
'''

code_block = '''
```json
{}
```
'''

url = 'https://graphql.anilist.co'

def embed(media):
    description = ""
    for medium in media:
        if medium["status"] in ["RELEASING", "NOT_YET_RELEASED"]:
            episodes = f"{medium['episodes']}" if medium['episodes'] else "?"
            episode = f"**{medium['nextAiringEpisode']['episode']}**/{episodes}"
            air_ts = medium['nextAiringEpisode']['airingAt']
            anilist_url = f"[AniList](https://anilist.co/anime/{medium['id']})"
            mal_url = f"[MAL](https://myanimelist.net/anime/{medium['idMal']})"
            description += f"**{medium['title']['romaji']}**\n{episode} <t:{air_ts}:f> (<t:{air_ts}:R>)\n{anilist_url}, {mal_url}\n\n"
    if description == "":
        description = "No planned anime is currently airing"
    e = discord.Embed(title="Next airing anime episodes", description=description)
    return e

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="airing")
    async def airing(self, ctx, username="same"):
        """For a given user, check their planned to watch anime and show the next episodes of the anime that is airing.
        User defaults to "same"
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={'query': watching_query, 'variables': {'name': username}}) as r:
                if r.status != 200:
                    await ctx.send("Couldn't get planned list from anilist :(")
                    return
                js = await r.json()
                list = sorted(
                    [x["media"] for x in js["data"]["MediaListCollection"]["lists"][0]["entries"] if x["media"]["nextAiringEpisode"]],
                    key=lambda x: x["nextAiringEpisode"]["airingAt"]
                )
        
        
        await ctx.send(embed=embed(list))

def setup(bot):
    bot.add_cog(Anime(bot))