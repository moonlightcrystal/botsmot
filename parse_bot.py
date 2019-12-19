from telethon import TelegramClient, events
import telethon 
import conbot as c
import logging
import socks
import base

logger = logging.getLogger('iris')

client = TelegramClient('kris', c.api_id, c.api_hash, **c.proxy, base_logger=logger)
client.start(phone='+79300091581')


# async def send():
#    await client.send_message('@yaroslav_saintp', 'Happy Birthday^ my friend! I am sending you this message from my own telegram bot and it says "DO IT.	JUST DO IT.	MAKE YOUR DREAMS COME TRUUE! 👊🏻"')
# client.loop.run_until_complete(send())

@client.on(events.NewMessage(pattern = r'^#startParse .+$'))
async def parse(event):
   namechannel = event.message.raw_text[12:]
   info = await client.get_entity(namechannel)
   history = await client.get_messages(info, 10)
   for message in history:
      print(message.stringify())

   # print(history)
   # users = await client.get_participants(info)
   # base.create_table()
   # base.feel_it(users)

   await event.reply('PARSE DONE WITH ' + namechannel)

client.loop(client.run_until_disconnected())

