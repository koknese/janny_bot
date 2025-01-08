import discord
from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
from dotenv import load_dotenv
from typing import Literal
import asyncio
from roblox import Client
import random
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
    patientID = 1325846599003541545
    role_patient = discord.Object(id=role_patient)
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
    else: # todo: add checking for nteraction user rol
        await interaction.response.send_message("Application not sent!", ephemeral=True)

@tree.command(
    name='verify',
    description='Verify your Roblox account by changing your description.',
    guild=discord.Object(id=server_id)
)
@app_commands.describe(id="ID of the account you want to verify as.")
async def verify(interaction: discord.Interaction, id: int):
    robloxUser = await robloxAPI.get_user(id)
    class Buttons(discord.ui.View):
        def __init__(self, *, timeout=180):
            super().__init__(timeout=timeout)
        @discord.ui.button(label="Finish verification",style=discord.ButtonStyle.green)
        async def finish_verification(self, interaction:discord.Interaction, view: discord.ui.View):
            await asyncio.sleep(2)  # wait for 3 seconds
            description = robloxUser.description # once button clicked, pull the users description and put it in a variable
            if description == sentence:
                embed.remove_field(0)
                embed.remove_footer(0)
                embed.add_field(name="Verified successfully!", value="Logging data, assigning roles...")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                logs = bot.get_channel(1326599452013756508)
                await logs.send(f"{interaction.user} just verified.", embed=embed)
            else:
                await interaction.response.send_message("Verification failed! Verify your data and try again! Notify hawktuahgamer if the bot still malfunctions.")

    embed = discord.Embed(title=f"Verifying as {robloxUser.name}", color=discord.Color.yellow())

    def createSentence():
        words = ["town", "verify", "cake", "centre", "bot", "rehabilitation"]
        return random.choice(words) + " " + random.choice(words)

    sentence = createSentence()

    embed.add_field(name="Edit your profile description to match ***exactly*** the following sentence.", value=f"`{sentence}`")
    embed.set_footer(text="Press the button after editing the description to finish verification.")
    await interaction.response.send_message(embed=embed, ephemeral=True, view=Buttons())


load_dotenv()
token = os.getenv('TOKEN')
bot.run(token)