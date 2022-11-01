import datetime

from aiogram import types

from fractions import DailyReport

async def send_report(message: types.Message, regexp_command):
    start_date = datetime.datetime(
        int(regexp_command.group('year')),
        int(regexp_command.group('month')),
        int(regexp_command.group('day')),
        )
    await message.answer(str(DailyReport(start_date)))   

