from IObserverModel import IObserverModel
from aiogram import Bot, types

class ViewObserverTelegram(IObserverModel):

    
    

    async def show_company_serched(self, bot: Bot, message: types.Message, resultModel: str):
        await bot.send_message(message.from_user.id, resultModel)
    