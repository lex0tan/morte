from telethon import TelegramClient, events

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

from pornhub_api import PornhubApi
from colorama import init, Fore
from com_list import *
import urllib.request
import subprocess
import pyfiglet
import asyncio
import random
import socket
import json
import time
import os

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    f = pyfiglet.Figlet(font="digital")
    logo = f.renderText("PORNHUBOT")
    print (random.choice(colors) + logo + rs + (f"""                {lg}Version 1.0{rs}
       tg: @arricchirmi | git: lex0tan"""))

def callback(current, total):
        print(f'{info}uploaded', current, 'on', total,
              'bytes: {:.0%}'.format(current / total))


sysname = os.getlogin()

api_id = 
api_hash = ""    
    

lg = Fore.LIGHTGREEN_EX
rs = Fore.RESET
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
colors = [lg, w, r, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error= lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '+' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
colors = [lg, w, r, cy]

