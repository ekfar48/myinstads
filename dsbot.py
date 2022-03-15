import os
import discord
from discord.ext import commands
from random import randint

from discord import Permissions
from discord.utils import get
from asyncio import sleep

##import pyautogui as pp
import os
##from pyffmpeg import FFmpeg
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
##from instabot import Bot
##import urllib.request
import datetime,pytz
import time
import requests
import webbrowser

client = commands.Bot(command_prefix=">",intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
        activity=discord.Game(">open,move,click")) 
        
@client.command()
async def open(ctx,arg1):
    #подключения драйвера
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('window-size=945,1030')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    
    driver.get(f"https://www.google.com/search?q={arg1}+aktie")
    driver.maximize_window()
    
    sleep(1)
    
    elem= driver.find_element_by_css_selector(".NprOob")
    elems= driver.find_element_by_css_selector(".WlRRw")
    print(elem.text)
    
    screenshot = driver.save_screenshot('my_screenshot.png')
#     await ctx.send(file=discord.File("my_screenshot.png"))
    


    im = Image.open('my_screenshot.png')
    sleep(1)
    im_crop = im.crop((10, 345, 690, 805))
    sleep(1)
    im_crop.save('guido_pillow_crop.png', quality=95)
    
#     await ctx.send(file=discord.File("guido_pillow_crop.png"))

    textil = elems.text
    lents = len(elems.text)
    bin = int(lents) - int(5)
    rel = textil[0:bin]
    print(textil[0:1])

    if str(textil[0:1]) == str("+"):
        embed_en = discord.Embed(title=f"▬▬▬▬▬▬▬▬[Акции {arg1}]▬▬▬▬▬▬▬▬", description=f"**Стоимость:** {elem.text} │ **просадок:** {rel}", color=0x3cd126)
    else:
        embed_en = discord.Embed(title=f"▬▬▬▬▬▬▬▬[Акции {arg1}]▬▬▬▬▬▬▬▬", description=f"**Стоимость:** {elem.text} │ **просадок:** {rel}", color=0xea4335)
        
#     await ctx.send(elem.text)
#     embed_en = discord.Embed(title=f"▬▬▬▬▬▬▬▬[Акции {arg1}]▬▬▬▬▬▬▬▬", description=f"**Стоимость:** {elem.text} │ **просадок:**fds", color=0xea4335)



    file = discord.File(r"guido_pillow_crop.png", filename="guido_pillow_crop.png")
    embed_en.set_image(url="attachment://guido_pillow_crop.png")

    
    await ctx.send(file=file, embed=embed_en)
    
    os.remove("my_screenshot.png")
    os.remove("guido_pillow_crop.png")

client.run(os.environ['token'])
