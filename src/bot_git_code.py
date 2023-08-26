import discord
from discord.ext import commands, tasks
from flask import Flask, request, jsonify

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@app.route('/github', methods=['POST'])
def github_event():
    payload = request.json
    commit_message = payload['commits'][0]['message']  # Extract the commit message from the first commit
    channel = bot.get_channel(YOUR_DISCORD_CHANNEL_ID)  # Replace with your Discord channel ID
    bot.loop.create_task(channel.send(f"New GitHub commit: {commit_message}"))
    return jsonify({'status': 'received'})

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Start the bot
bot.run('YOUR_DISCORD_BOT_TOKEN', bot=False)  # Replace with your Discord bot token
