from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.reply_keyboard import KeyboardButton
from aiogram.utils import executor

import config as cf 
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(cf.TOKEN)
dp = Dispatcher(bot)


yes_btn = KeyboardButton('/yes')
no_btn = KeyboardButton('/no')

markup = ReplyKeyboardMarkup(resize_keyboard=True).row(yes_btn, no_btn)

def change_yes_state(state):
    cf.state = dict(cf.state.get('yes'))

def change_no_state(state):
    cf.state = dict(cf.state.get('no'))

def change_start_state(state):
    cf.state = cf.tree['dtp']

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    change_start_state(cf.state)
    await message.reply(cf.start_message, reply_markup=markup)

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, parse_mode='HTML', text=cf.help_message)

@dp.message_handler(commands=["no"])
async def yes(message: types.Message):
    change_no_state(cf.state)
    await message.reply(cf.state.get('text'))

@dp.message_handler(commands=["yes"])
async def yes(message: types.Message):
    change_yes_state(cf.state)
    await message.reply(cf.state.get('text'))
    

if __name__ == '__main__':
    executor.start_polling(dp)