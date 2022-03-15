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
from selenium.webdriver.firefox.options import Options
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
async def open(ctx,insta="morgen_shtern"):
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN") 
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--no-sandbox") 
    ##chrome_options.add_argument("--start-maximized") 
    chrome_options.add_argument('window-size=945,1030') 
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options) 
    driver.get(f"https://www.instagram.com/{insta}") 
    #driver.maximize_window()
    ##
    screenshot = driver.save_screenshot('my_screenshot.png')
    ##await ctx.send(file=discord.File("my_screenshot.png"))

    embed_en = discord.Embed(title=f"text", description=f"**txtz", color=0xea4335)
    embed_en.set_image(url="attachment://my_screenshot.png") 

    file = discord.File(r"my_screenshot.png", filename="my_screenshot.png")
    await ctx.send(file=file,embed=embed_en)
    
client.run(os.environ['token'])
