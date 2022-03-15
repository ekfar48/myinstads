import os
import discord
from discord.ext import commands
from random import randint

from discord import Permissions
from discord.utils import get
from asyncio import sleep

import pyautogui as pp
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
async def open(ctx,arg1="morgen_shtern"):
    #подключения драйвера
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    ##chrome_options.add_argument('window-size=945,1030')
    driver = webdriver.Chrome(executable_path=str(os.environ.get("CHROMEDRIVER_PATH")), chrome_options=chrome_options)       
    driver.get(f"https://www.instagram.com/{arg1}")
    driver.maximize_window()    
    sleep(1)  
    screenshot = driver.save_screenshot('my_screenshot.png')


    im = Image.open('my_screenshot.png')
    im.save('guido_pillow_crop.png', quality=95)   
    embed_en = discord.Embed(title="text",description="desc", color=0xea4335)
    file = discord.File(r"guido_pillow_crop.png", filename="guido_pillow_crop.png")
    embed_en.set_image(url="attachment://guido_pillow_crop.png")

    
    await ctx.send(file=file, embed=embed_en)
    
    os.remove("my_screenshot.png")
    os.remove("guido_pillow_crop.png")

@client.command()
async def move(ctx,xy):

    a = xy.split(",")

    pp.moveTo(int(a[0]),int(a[1]))



    screenshot = driver.save_screenshot('my_screenshot.png')
    im = Image.open('my_screenshot.png')
    im.save('guido_pillow_crop.png', quality=95)   
    embed_en = discord.Embed(title="text",description="desc", color=0xea4335)
    file = discord.File(r"guido_pillow_crop.png", filename="guido_pillow_crop.png")
    embed_en.set_image(url="attachment://guido_pillow_crop.png") 
    await ctx.send(file=file, embed=embed_en)   
    os.remove("my_screenshot.png")
    os.remove("guido_pillow_crop.png")





client.run(os.environ['token'])
