import discord
from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
from dotenv import load_dotenv
import os
# Intents
intents = discord.Intents.all()
intents.members = True
server_id = 1325475721459798156

bot = commands.Bot(command_prefix="sudo ", intents=intents)
tree = bot.tree

# Load cogs
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await tree.sync(guild=discord.Object(id=server_id))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"over the Town Rehab Conglomerate"))
    print(discord.__version__)

@bot.event
async def on_member_join(member):
    role_patient = 1325846599003541545
    await member.add_roles(role_patient)

@tree.command(
        name='hello',
        description='haii',
        guild=discord.Object(id=server_id)
)
async def hello (interaction: discord.Interaction):
		await interaction.response.send_message("guh")


load_dotenv()
token = os.getenv('TOKEN')
bot.run(token)