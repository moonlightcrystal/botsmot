from telethon import TelegramClient
import telethon 
import conbot as c
import logging
import socks

logger = logging.getLogger('iris')

client = TelegramClient('kris', c.api_id, c.api_hash, base_logger=logger)
client.start(phone='+79300091581')


async def send():
   await client.send_message('@ktgri', 'Hello Beaty Girl YOU ARE BEST')

client.loop.run_until_complete(send())