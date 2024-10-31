import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import View
from join_button import JoinButton, LeaveButton, clear_queue

import random as r

# STEP 0: Load token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

queue = []

def run():
    # STEP 1: Bot setup
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready for use!")
        print("-----------------------")
    
    # @bot.event
    # async def on_message(message) -> None:
    #     await bot.process_commands(message)
    #     if message.author == bot.user:  # If the author is the bot itself, end loop
    #         return
        
    #     username = str(message.author)
    #     user_message = message.content
    #     channel = str(message.channel)

    #     print(f'[{channel}] {username}: "{user_message}"')

    @bot.command()
    async def hello(ctx):
        await ctx.send("pong")

    @bot.command()
    async def random(ctx):
        num = r.randint(1, 6)
        await ctx.send(f"You rolled: {num}")

    @bot.command()
    async def embedqueue(ctx):
        embed = discord.Embed(
            colour=discord.Colour.brand_red(),
            description="Queue System | Valorant",
            title="Monash Esports Club",
        )
        
        embed_message(embed)

        view = View(timeout=None)
        join_button = JoinButton()
        leave_button = LeaveButton()
        view.add_item(join_button)
        view.add_item(leave_button)

        await ctx.send(embed=embed, view=view)

    @bot.command()
    async def clearqueue(ctx):
        clear_queue()
        # Fetch the message where the embed is, assuming the command is used in the same channel
        async for message in ctx.channel.history(limit=200):
            if message.author == bot.user and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Monash Esports Club":
                    embed.clear_fields()
                    embed_message(embed)
                    await message.edit(embed=embed)
                    break

        await ctx.send("The queue has been cleared.")\
        
    def embed_message(embed):
        embed.add_field(name='Time', value='Friday, 9PM (GMT+8)', inline=False)
        embed.add_field(name='#', value='\u200b', inline=True)
        embed.add_field(name='Riot ID', value='\u200b', inline=True)
        embed.add_field(name='Discord', value='\u200b', inline=True)
        # Add the image at the bottom of the embed
        embed.set_image(url='https://cdn.discordapp.com/attachments/1235203268003631164/1275822707992166422/valorant.png?ex=66c749fd&is=66c5f87d&hm=1da95107153dde173452e6f58cd663eae7ad0de75a0e596ab5ab7490b15a53aa&')


    bot.run(TOKEN)


if __name__ == '__main__':
    run()
