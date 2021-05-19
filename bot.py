from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, first_message

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, parse_mode='HTML', text=first_message)

if __name__ == '__main__':
    executor.start_polling(dp)