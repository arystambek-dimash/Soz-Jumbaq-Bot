from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
import sozder,random,requests
from config import TOKEN
from sozder import rand_soz,HELP_COMMAND,EREJE_COMMAND
from aiogram import  executor, Bot, Dispatcher
from database import BotDB
"""Main"""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
"""DATABASE"""
BotDB = BotDB("DATABASE")
"""Peremenny"""
soz = rand_soz
username = ''
game_start = False
raiting = 1
point = 1
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
    if(not  BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id,message.from_user.first_name)
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
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id, message.from_user.first_name)
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
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id, message.from_user.first_name)
    global username,soz
    if message.text == soz:
        soz = sozder.clear_sozdik[sozder.rand_soz_int-2]
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
        rand_int = random.randint(0, 6)

        r = requests.get(sozder.URL[rand_int])
        s = sozder.bs(r.text, "html.parser")
        sozdik = s.find_all('div', class_="row_word")
        clear_sozdik = [c.text for c in sozdik]
        soz = clear_sozdik[sozder.random.randint(1, sozder.rand_soz_int - 1)]
""""""
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)