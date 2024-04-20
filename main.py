import discord
import logging
from config import TOKEN
import requests

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

TOKEN = TOKEN


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "кот" in message.content.lower():
            await message.channel.send(requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url'])
        if any(pes in message.content.lower() for pes in ['пёс', 'соба']):
            await message.channel.send(requests.get('https://dog.ceo/api/breeds/image/random').json()['message'])


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
