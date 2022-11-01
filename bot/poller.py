import logging

from aiogram import Bot, Dispatcher, types, filters

from settings import TG_BOT_API_TOKEN



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TG_BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

from bot.report import send_report

send_report = dp.message_handler(
    filters.RegexpCommandsFilter(regexp_commands=['report_(?P<year>\d{4})_(?P<month>\d{2})_(?P<day>\d{2})'])
)(send_report) 
