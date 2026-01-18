import os
import discord
from discord.ext import commands
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

@bot.command()
async def test(ctx):
    embed = discord.Embed(
        title="🧪 Gorilla Tag Update Bot – Test",
        description="Embed system is working correctly.",
        color=0x00ff88,
        timestamp=datetime.now(timezone.utc)
    )

    embed.add_field(
        name="Status",
        value="✅ Online\n✅ Embeds OK\n✅ Railway OK",
        inline=False
    )

    embed.set_footer(text="GTAG Update Tracker")

    await ctx.send(embed=embed)

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set")

bot.run(TOKEN)
