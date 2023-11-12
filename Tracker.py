import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

download_dir = "attachments"
os.makedirs(download_dir, exist_ok=True)

log_file = "log.txt"

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    log_message = f"Message from {message.author}: {message.content}\n"
    print(log_message)

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(log_message)

    for attachment in message.attachments:
        print(f"Media file attached: {attachment.url}")
        
        download_path = os.path.join(download_dir, attachment.filename)
        
        await attachment.save(download_path)
        print(f"Downloaded file saved at: {download_path}")

client.run('YOUR TOKEN')
