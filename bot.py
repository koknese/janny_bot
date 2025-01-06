import discord
from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
from dotenv import load_dotenv
from typing import Literal
import asyncio
from roblox import Client
import os
intents = discord.Intents.all()
intents.members = True
server_id = 1325475721459798156
robloxAPI = Client()
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


@tree.command(
        name='staffapplication',
        description='Apply to become facility staff. Most people are expected to be accepted!',
        guild=discord.Object(id=server_id)
)
@app_commands.describe(id="Roblox ID", verify="You have verified that your ROBLOX ID is correct.")
async def staffapplication (interaction: discord.Interaction, id: int , verify: Literal["No", "Yes"]):
    if verify == "Yes":
        embed = discord.Embed(title="Facility Staff Application sent!", color=discord.Color.yellow())
        embed.add_field(name="Provided ID", value=id, inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        robloxUser = await robloxAPI.get_user(id)
        embed = discord.Embed(title="Facility Staff Application received!", color=discord.Color.yellow())
        embed.add_field(name=f"ROBLOX Username", value=robloxUser.name, inline=True)
        embed.add_field(name=f"ROBLOX Display Name", value=robloxUser.display_name, inline=True)
        embed.add_field(name=f"Discord username?", value=interaction.user, inline=True)
        applicationChannel = bot.get_channel(1325864260051534005)
        await applicationChannel.send(embed=embed)
    else: # todo: add checking for nteraction user role
        await interaction.response.send_message("Application not sent!", ephemeral=True)


load_dotenv()
token = os.getenv('TOKEN')
bot.run(token)