import discord


def format_date(d):
    return d.strftime("%a %d. %B %Y, %H:%M UTC")


def embed(user, name):
    e = discord.Embed(title=name, colour=user.colour)
    e.set_footer(text=f"{user.name}#{user.discriminator} ({user.id})")
    e.set_image(url=user.display_avatar.url)
    e.add_field(name="Status", value=user.status, inline=True)
    e.add_field(name="Registered", value=format_date(user.created_at), inline=True)
    e.add_field(name="Joined", value=format_date(user.joined_at), inline=True)
    if user.bot:
        e.description = "Bot"
    if user.premium_since:
        e.add_field(
            name="Boosted server", value=format_date(user.premium_since), inline=True,
        )
    for activity in user.activities:
        if activity.type == discord.ActivityType.listening:
            e.add_field(
                name="Listening to",
                value=f"[{activity.artist} - {activity.title}](https://open.spotify.com/track/{activity.track_id})",
                inline=True,
            )
        if activity.type == discord.ActivityType.playing:
            e.add_field(name="Playing", value=activity.name, inline=True)
        if activity.type == discord.ActivityType.streaming:
            e.add_field(
                name="Streaming",
                value=f"[{activity.game} ({activity.name})]({activity.url})",
                inline=True,
            )
        if activity.type == discord.ActivityType.custom:
            e.add_field(name="Playing?", value=activity.name, inline=True)
    return e

