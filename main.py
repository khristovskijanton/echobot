import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

# Установите свой токен бота
API_TOKEN = "6502670177:AAEOP56LypLvvsTQW9v8WnjFV_UyUwDa9Ys"
WEBHOOK_URL = "https://echobot.mooo.com"  # Замініть це на свій URL

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    #await bot.send_message(chat_id=5577002380, text='Бот запущений')

async def on_shutdown(dp):
    await bot.delete_webhook()
    #await bot.send_message(chat_id=5577002380, text='Бот остановлен')

# Хендлер на команду /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я эхо-бот. Просто отправь мне сообщение, и я повторю его.")

# Хендлер на любое текстовое сообщение
@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: types.Message):
    # Отправка эхо-сообщения
    await message.answer(f"Вы написали: {message.text}")

# Запуск бота с использованием метода поллинга
if __name__ == '__main__':
    from aiogram import executor

    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=5000)
