import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("TOKEN")

if not token:
    raise ValueError("No TOKEN found in environment variables.")


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in successfully as: {client.user} (ID: {client.user.id})")
    await client.close()

client.run(token)