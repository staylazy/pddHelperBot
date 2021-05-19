from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config as cf 

bot = Bot(cf.TOKEN)
dp = Dispatcher(bot)

def change_yes_state(state):
    cf.state = dict(cf.state.get('yes'))

def change_no_state(state):
    cf.state = dict(cf.state.get('no'))

def change_start_state(state):
    cf.state = cf.tree['dtp']

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    change_start_state(cf.state)
    await message.reply(cf.state)

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, parse_mode='HTML', text=cf.help_message)

@dp.message_handler(commands=["no"])
async def yes(message: types.Message):
    change_no_state(cf.state)
    print(cf.state.get('text'))
    await message.reply(cf.state.get('text'))

@dp.message_handler(commands=["yes"])
async def yes(message: types.Message):
    change_yes_state(cf.state)
    print(cf.state.get('text'))
    await message.reply(cf.state.get('text'))
    

if __name__ == '__main__':
    executor.start_polling(dp)