import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

# Установите свой токен бота
API_TOKEN = "6502670177:AAEOP56LypLvvsTQW9v8WnjFV_UyUwDa9Ys"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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

    executor.start_polling(dp, skip_updates=True)
