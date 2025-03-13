import sys
import discord
from discord.ext import commands

token = sys.argv[1] if len(sys.argv) > 1 else "ADMIN123"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} siap digunakan!')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

bot.run(token)
