import telegram
import asyncio
import time
from message_utils import read_message_from_file
from config import TELEGRAM_TOKEN

class TelegramBot:
    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_TOKEN)

    def read_message_from_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    async def send_messages(self, group_id, messages, time_delay, duration):
        start_time = time.time()
        elapsed_time = 0

        while elapsed_time < duration:
            for message in messages:
                await self.bot.send_message(chat_id=group_id, text=message)
                await asyncio.sleep(time_delay)

            elapsed_time = time.time() - start_time