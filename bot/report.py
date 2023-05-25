import datetime

from aiogram import types, filters

from common_fractions import DailyReport, DailyReportUntil
from bot.bot import dp

@dp.message_handler(
    filters.RegexpCommandsFilter(regexp_commands=['report_(?P<year>\d{4})_(?P<month>\d{2})_(?P<day>\d{2})'])
)
async def send_report(message: types.Message, regexp_command):
    start_date = datetime.datetime(
        int(regexp_command.group('year')),
        int(regexp_command.group('month')),
        int(regexp_command.group('day')),
        )
    await message.answer(str(DailyReport(start_date)))   

@dp.message_handler(
    filters.RegexpCommandsFilter(regexp_commands=['report_until_(?P<year>\d{4})_(?P<month>\d{2})_(?P<day>\d{2})'])
)
async def send_report_until(message: types.Message, regexp_command):
    start_date = datetime.datetime(
        int(regexp_command.group('year')),
        int(regexp_command.group('month')),
        int(regexp_command.group('day')),
        )
    await message.answer(str(DailyReportUntil(start_date)))   


