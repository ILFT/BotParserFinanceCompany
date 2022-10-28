
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command

import sys
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\model')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\model\companyModel')
print(sys.path)

from model.parserFinanceIndicators import ParserFinanceIndicators
from model.companyModel.company import Company

#import os
#import token

TOKEN_API_TELEGRAM = ''

class TelegramView():

    def show():
        pass

bot = Bot(token=TOKEN_API_TELEGRAM)
dp = Dispatcher(bot)

@dp.message_handler(commands=['search'])
async def search_company(message: types.Message, command: Command):
    company = ParserFinanceIndicators.parsing(command.args) 
    if company == None:
        await message.answer('company not found')
    else:
        await message.answer(company.get_price_to_earnings())

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True)