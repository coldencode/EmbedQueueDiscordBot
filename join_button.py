import asyncio
import discord
from discord.ui import Modal, TextInput, Button, View
from join_button import embed_message

queue = []

def clear_queue():
    global queue
    queue = []

class InputModal(Modal):
    def __init__(self):
        super().__init__(title="Join Queue")
        
        self.riot_id = TextInput(
            label="Please enter your Riot ID:",
            placeholder='e.g. coldeN#val',
        )
        
        self.add_item(self.riot_id)
        # self.add_item(self.rank)

    async def on_submit(self, interaction: discord.Interaction):
        if '#' not in self.riot_id.value:
            await interaction.response.send_message("Error: Riot ID must contain a `#` symbol. Please try again.", ephemeral=True)
            new_modal = InputModal()
            await interaction.response.send_modal(new_modal)
            return
        
        for user in queue:
            if user['id'] == interaction.user.id:
                await interaction.response.send_message("You are already in the queue!", ephemeral=True)
                return
            
        queue.append({'id': interaction.user.id, 'riot_id': self.riot_id.value, 'mention': interaction.user.mention})

        # Update the embed message
        embed = interaction.message.embeds[0]
        embed.clear_fields()
        embed_message(embed)

        await interaction.message.edit(embed=embed)
        await interaction.response.send_message("You have been added to the queue!", ephemeral=True)

class JoinButton(Button):
    def __init__(self):
        super().__init__(label="Join", style=discord.ButtonStyle.success)

    async def callback(self, interaction: discord.Interaction):
        modal = InputModal()
        await interaction.response.send_modal(modal)

class LeaveButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Leave", style=discord.ButtonStyle.danger)

    async def callback(self, interaction: discord.Interaction):
        user_in_queue = next((user for user in queue if user['id'] == interaction.user.id), None)
        if user_in_queue is None:
            await interaction.response.send_message("You are not in the queue!", ephemeral=True)
            return

        queue.remove(user_in_queue)

        # Update the embed message
        embed = interaction.message.embeds[0]
        embed.clear_fields()
        embed.add_field(name='Time', value='Friday, 9PM (GMT+8)', inline=False)
        embed.add_field(name='#', value=''.join(f'{idx+1}\n' for idx in range(len(queue))), inline=True)
        embed.add_field(name='Riot ID', value=''.join(f'{user["riot_id"]}\n' for user in queue), inline=True)
        embed.add_field(name='Discord', value=''.join(f'{user["mention"]}\n' for user in queue), inline=True)

        # Ensure the embed retains the image
        embed.set_image(url='https://cdn.discordapp.com/attachments/1235203268003631164/1275822707992166422/valorant.png?ex=66c749fd&is=66c5f87d&hm=1da95107153dde173452e6f58cd663eae7ad0de75a0e596ab5ab7490b15a53aa&')

        await interaction.message.edit(embed=embed)
        await interaction.response.send_message("You have been removed from queue!", ephemeral=True)
        return
