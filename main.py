import logging
import aioschedule
import asyncio
import random
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6577993420:AAEodcQhu450nDsQK97EzA8WFJjc4MEjz30'
CHAT_ID = '-1001968484864' # ПОМЕНЯТЬ ПОТОМ!!!!

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if str(message.from_user['id']) == '772424455':
        await message.answer('Маргонафт обнаружен')
    else:
        await message.answer("ты не Маргонафт")
    print(message.chat.id)


# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message.chat.id)
#     if str(message.from_user['id']) == '772424455': #'1059667959' - moy id; '772424455' - id margoshi:
#         await message.answer('Маргоша ты няша')
#         await StateGroupExample.wait_for_answer.set()
#     else:
#         await message.answer(message.text)
#         await StateGroupExample.wait_for_answer.set()


# @dp.message_handler()
# async def reply(message: types.Message):
#     if str(message.from_user['id']) == '772424455':
#         await message.answer('Маргонафт обнаружен')
#     else:
#         await message.answer("ты не Маргонафт")


async def send_goodnight():
    text = 'спокойной ночи Мишутка, Кирюша, Ксюшенькии, Ренаточка,Вадимчик, Артемчик, Ванечка, Маргоша, Анварчик, Савельчик, Тимурчик, Арсенчик, Данильчик, Линарчик, Аксюнья, Таечка,Равилька, Ромочка, Ириночка, Ясминчик, Машечка,Катюша, Марсельчик и Ясминочка!!!❤️❤️❤️'
    await bot.send_message(CHAT_ID, text)
    await bot.send_message(CHAT_ID, "Маргоша ты няша ♥♥♥")


async def send_goodmorning():
    text = "Доброе утро ♥♥♥"
    await bot.send_message(CHAT_ID, text)
    await bot.send_message(CHAT_ID, "Маргоша ты няша ♥♥♥")


async def scheduler():
    aioschedule.every().day.at("00:30").do(send_goodnight)
    aioschedule.every().day.at("12:23").do(send_goodmorning)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp): 
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)