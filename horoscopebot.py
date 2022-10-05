import discord
from discord import app_commands
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
greeting = ['Hello', 'Sup', 'Howdy', 'Hi', 'Hola', 'Greetings', 'Namaste']
def get_horo(horoscope):

    horo_dict = {'aries':1, 'taurus':2,'gemini':3,'cancer':4,'leo':5,'virgo':6, 'libra':7,'scorpio':8,'sagittarius':9,'capricorn':10,'aquarius':11,'pisces':12}
    try:
        i = horo_dict[horoscope.lower()]
    except:
        flag = 0
        return (0, 'Invalid Input!')

    URL = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={i}"
    try:
        page = requests.get(URL)
    except:
        page = 'F'
        return (1, 'Could not retrieve horoscope')

    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find('p')
    return(2, p.get_text())

@bot.event
async def on_ready():
    print("READY")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="horoscope")
@app_commands.describe(horoscope="What is your star sign?")
async def horoscope(interaction: discord.Interaction, horoscope: str):

    flag, txt = get_horo(horoscope)
    if flag == 0:
        await interaction.response.send_message(f"{horoscope} is not a valid horoscope!")
    elif flag == 1:
        await interaction.response.send_message(f"{txt}")
    else:
        value = random.choice(greeting)
        await interaction.response.send_message(f"{value}, {interaction.user.mention} here's your daily horoscope: {txt}")

bot.run('MTAyNzMwMTczODU0MzMyOTMxMA.G-fplC.87KtDgGZ6KSNxXKphGeara86a0MWEdpASCAxCM')