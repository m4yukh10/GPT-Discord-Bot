import discord
import requests
import json
import random
from openai import OpenAI
import os

intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)


openai_client = OpenAI(api_key=os.environ['OPENAI_API'])

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = '"' + json_data[0]['q'] + '"' + " - " + json_data[0]['a']
    return quote

def use_gpt(msg):
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}],
        max_tokens = 500,
        temperature = 0.5
    )
    return completion.choices[0].message.content

@discord_client.event
async def on_ready():
    print(f"We have logged in as {discord_client.user}")

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        return

    msg = message.content

    if message.content.lower().startswith("inspire kor amay"):
        quote = get_quote()
        await message.channel.send(quote)
    else:
        response = use_gpt(msg)
        await message.channel.send(response)
discord_client.run(os.environ['DISCORD_TOKEN'])  
