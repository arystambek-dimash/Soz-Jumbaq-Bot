from aiogram import Bot,Dispatcher,executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, KeyboardButton,\
    InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
import sqlite3 as sq
import sozder
from config import TOKEN
from sozder import rand_soz,HELP_COMMAND,EREJE_COMMAND
from aiogram.types import CallbackQuery
from database import *
from aiogram import  types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
"""Main"""
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot,storage=storage)
"""Peremenny"""
soz = rand_soz
username = ''
game_start = False
"""STATE"""
class ProfileStatesGroup(StatesGroup):
    firstname,raiting,tap_soz,tus_soz = State(),State(),State(),State()
"""INLINE"""
def get_ikb()->InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton('Botty chatqa qosu➕',url='t.me/soz_jumbaq_bot?startgroup=botstart')]
    ])
    return ikb
"""INLINE"""
ikb_soz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Sozdi koru👀',callback_data='sozdi_koru')],
    [InlineKeyboardButton('Kelesi soz⏭️⏭️',callback_data='kelesi_soz')]
])
"""START"""
@dp.message_handler(commands=['bastau','start'])
async def start_command(message:Message):
    await bot.send_message(chat_id=message.from_user.id,text = "Sälem!👋 Men Söz-Jūmbaq oiynyn jürgızetın bolamyn🤓.",reply_markup=get_ikb())
"""HELP"""
@dp.message_handler(commands=['komek','help','помощь'])
async def help_command(message :Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()
"""RULES"""
@dp.message_handler(commands=['ereje','rules','правила'])
async def ereje_command(message:Message):
    await message.answer(EREJE_COMMAND)
    await message.delete()
"""OINAU"""
@dp.message_handler(commands = ['oinau','play','играть'])
async def oynau_command(message:Message):
    global game_start,username
    if game_start == False:
        await bot.send_message(chat_id=message.chat.id,text = f"{message.from_user.first_name} soz jasurady",reply_markup=ikb_soz)
        username = message.from_user.first_name
        game_start = True
    else:
        await bot.send_message(chat_id=message.chat.id, text="Oyin bolyp jatyr🙃")
"""TOQTATU"""
@dp.message_handler(commands=['toqta','stop','cancel','стоп'])
async def cancel_command(message:Message):
    global game_start
    if game_start == True:
        await bot.send_message(chat_id=message.chat.id,text="Oyin toqtayldi☹️")
        await message.delete()
        game_start = False
    else:
        await bot.send_message(chat_id=message.sender_chat.id,text='Oyin bastalmagan🙄')
"""MESSAGE """
@dp.message_handler()
async def soz_command(message : Message):
    global username,soz
    if message.text == soz and message.from_user.first_name != username:
        await bot.send_message(chat_id=message.chat.id,text = f"{message.from_user.first_name} soz tapbyldi👍\nKelesi soz🫡",reply_markup=ikb_soz)
        username = message.from_user.first_name
"""CALLBACK"""
@dp.callback_query_handler()
async def koru(callback:CallbackQuery):
    global soz
    if callback.data == 'sozdi_koru' and callback.from_user.first_name == username:
        await callback.answer(show_alert=True,text=f"Jasyrin Soz🤫: {soz}")
    elif callback.from_user.first_name == username:
        await callback.answer(text = "soz ozgerdi")

        soz = sozder.clear_sozdik[sozder.random.randint(1, sozder.rand_soz_int - 1)]
""""""
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)