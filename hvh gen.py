import discord
from discord import app_commands
import random

# Set up bot intents
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# Pre-defined list of HVH profile picture URLs
HVH_PFP_URLS = [
    "https://infocheats.net/data/avatars/o/74/74828.jpg?1615059466",  # Replace with actual URLs
    "https://i.pinimg.com/236x/46/d0/a1/46d0a1bff7bf5d6e3783d3fb828e18d7.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4JRD-NeYGDEojZEfcM1YgwLTMKqWnZ5zTQ&s",
    "https://forum.neverlose.cc/uploads/default/original/3X/9/2/92f7afa1634effd1dd244e40bce4cff882530ce3.jpeg",
    "https://forum.neverlose.cc/uploads/default/original/3X/b/6/b6b92835ad4272090014d734f9a431808c55fe65.jpeg",
    "https://forum.neverlose.cc/uploads/default/original/3X/0/b/0b88d413784561b75b1ec7eb1f322b0d917791d0.jpeg",
    "https://steamuserimages-a.akamaihd.net/ugc/875246284888489362/8053D2D3A2AA2FD9E1E1C26CB74A84F7BE8322FE/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
    "https://i.imgur.com/2qzkeDB.jpeg",
    "https://i.imgur.com/3PtnfyU.jpeg",
    "https://www.themebeta.com/files/picture/201808/18/efe2edc0e2d9ff5fc85a7ff62f2f61e6.jpeg",
    "https://i.imgur.com/3IIw7zO.jpeg",
    "https://i.imgur.com/WPFr5GN.jpeg",
    "https://steamuserimages-a.akamaihd.net/ugc/784107399678250495/18F5ED8DA9FEB5F9D07B363726F4C7456B4D031A/",
    "https://avatars.fastly.steamstatic.com/47708fea059581e968a3b582ca008c3cdced586b_full.jpg",
    # Add more image links here
]

@bot.event
async def on_ready():
    await tree.sync()  # Sync commands with Discord
    print(f"Bot is online as {bot.user}")

@tree.command(name="hvhpfp", description="Fetches a random HVH profile picture.")
async def hvhpfp(interaction: discord.Interaction):
    """Slash command to fetch a random HVH profile picture."""
    if HVH_PFP_URLS:
        random_url = random.choice(HVH_PFP_URLS)
        await interaction.response.send_message(f"Here is a random HVH profile picture: {random_url}")
    else:
        await interaction.response.send_message("No HVH profile pictures available right now.")

# Run the bot
bot.run("YOUR DISCORD BOT TOKE HERE")
