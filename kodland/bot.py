import discord
from discord.ext import commands
import gen_pass

# Zmienna intents przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')

@bot.command()
async def password(ctx, pass_len = 10):
    await ctx.send(str(gen_pass.gen_pass(pass_len)))
bot.run("TWUJ TOKEN")