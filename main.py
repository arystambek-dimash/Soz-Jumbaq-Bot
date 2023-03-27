from aiogram import Bot,Dispatcher,executor
from aiogram.types import Message, KeyboardButton,\
    InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
import random

import sozder
from config import TOKEN
from sozder import rand_soz,HELP_COMMAND,EREJE_COMMAND
from aiogram.types import CallbackQuery

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
dp.message_handler(commands='start')
def get_ikb()->InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton('Botty chatqa qosu➕',callback_data='qosu')]
    ])
    return ikb

@dp.message_handler(commands=['bastau'])
async def start_command(message:Message):
    await bot.send_message(chat_id=message.from_user.id,text = "Sälem! Men Söz-Jūmbaq :D oiynyn jürgızetın bolamyn.",reply_markup=get_ikb())
@dp.message_handler(commands=['komek'])
async def help_command(message :Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()
@dp.message_handler(commands=['ereje'])
async def ereje_command(message:Message):
    await message.answer(EREJE_COMMAND)
    await message.delete()
isGame = False
text = ''

ikb_soz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Sozdi koru',callback_data='sozdi_koru')],
    [InlineKeyboardButton('Kelesi soz',callback_data='kelesi_soz')]
])

@dp.message_handler(commands = ['oinau'])
async def oynau_command(message:Message):
    await bot.send_message(chat_id=message.chat.id,text = f"{message.from_user.first_name} soz jasurady",reply_markup=ikb_soz)
    username = message.from_user.first_name


@dp.callback_query_handler()
async def koru(callback:CallbackQuery):
    global soz
    if callback.data == 'sozdi_koru' and callback.from_user.first_name == callback.message.md_text:
        await callback.answer(show_alert=True,text=f"soz: {soz}")
    elif callback.from_user.first_name == callback.message.md_text:
        await callback.answer(text = "soz ozgerdi")
        soz = sozder.clear_sozdik[sozder.random.randint(1, sozder.rand_soz_int - 1)]
@dp.message_handler()
async def soz_command(message : Message):
    if message == text:
        await bot.send_message(chat_id=message.chat.id,text = f"{message.from_user.first_name} soz tapty\n kelesi soz" )
        await  message.answer(text)


# @dp.callback_query_handler(text = 'qosu')
# async def qosu_command(callback : CallbackQuery):
#     await bot.

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)