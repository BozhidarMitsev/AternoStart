import os
import time
import random
import discord
from discord.ext import commands
from discord import app_commands
from python_aternos import Client

# Get sensitive information from environment variables
ATERNOS_USERNAME = input("Input Aternos Username (case sensetive): ")
ATERNOS_PASSWORD = input("Aternos Password (case sensetive): ")
ATERNOS_SERVER_DOMAIN = input("Input the server domain you wish to start up in your server (It should be the example from example.aternos.me): ")
DISCORD_BOT_TOKEN = input("Input your bot token: ")
VERSION = "V1.0 RELESE!!!"
CHANGELOG = "Bug fixes and preformance fixes"

# ATERNOS_USERNAME = os.environ.get('ATERNOS_USERNAME')
# ATERNOS_PASSWORD = os.environ.get('ATERNOS_PASSWORD')
# ATERNOS_SERVER_DOMAIN = os.environ.get('ATERNOS_SERVER_DOMAIN')
# DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
# SECURITY_PHRASE = os.environ.get('SECURITY_PHRASE')

print(f"Welcome to Server starter {VERSION} by Som#2014, please check regularly on the github page for updates and if you have any questions my dms are open in dicord\n"\
    f"New stuff are: {CHANGELOG}\n"\
    "\n"\
    "\n"\
    "Starting up....")
time.sleep(0.6)
# Aternos Auth and var
at = Client.from_credentials(ATERNOS_USERNAME, ATERNOS_PASSWORD)
servers = at.list_servers()
serv = next(
    (s for s in servers if s.subdomain == ATERNOS_SERVER_DOMAIN),
    None
)

if serv is None:
    print('Server not found!')
    exit()

print("Aternos Login done")

# Discord Bot
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!!')

@bot.event
async def on_ready():
    print('Bot is online!')

@bot.command()
async def start(ctx):
    await ctx.send(f"Starting server: {ATERNOS_SERVER_DOMAIN}.aternos.me")
    print(f"Someone used Start")
    serv.start()

@bot.command()
async def stop(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send(f"Stopping server: {ATERNOS_SERVER_DOMAIN}.aternos.me")
        print(f"Someone used Stop")
        serv.stop()
    else:
        await ctx.send("You don't have the permissions to perform this action.")

@bot.command()
async def version(ctx):
    await ctx.send(f"{VERSION}, Changelog: {CHANGELOG}")
    print(f"Someone used Version")

@bot.command()
async def status(ctx):
    await ctx.send("Bot is online for sure")
    print(f"Someone used Status")

@bot.command()
async def ip(ctx):
    await ctx.send(f"IP is: {ATERNOS_SERVER_DOMAIN}.aternos.me")
    print(f"Someone used Ip")

@bot.command()
async def cmds(ctx):
    message = "Commands you can use are:\n" \
              "!!start - Start the server\n" \
              "!!stop - Stopping the server (admin only)\n" \
              "!!version - Show the bot version\n" \
              "!!status - Show if the bot is online\n" \
              "!!ip - Show the bot IP\n" \
              "!!cmds - Show this message"
    print(f"Someone used cmds")
    await ctx.send(message)

@bot.command()
async def exit(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("Shutting down bot...")
        print(f"Shutting down bot with !!exit")
        time.sleep(5)
        await bot.close()
bot.run(DISCORD_BOT_TOKEN)
