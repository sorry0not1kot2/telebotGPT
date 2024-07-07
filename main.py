# файл main.py
import os
import asyncio
import logging
from telebot.async_telebot import AsyncTeleBot
import handlers
from translations import translations  # Импортируем translations как словарь

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Настройка бота
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = AsyncTeleBot(BOT_TOKEN)

# Обработчик команды /start
async def start(message):
    приветствие = translations['start']  # Используем переменную из translations
    await bot.send_message(message.chat.id, f"{приветствие} Слушаю тебя.")

# Добавление обработчиков
bot.register_message_handler(start, commands=['start'])
bot.register_message_handler(lambda message: handlers.handle_text(bot, message), content_types=['text'])

# Асинхронная функция main для запуска бота
async def main():
    logging.info("Бот запущен")
    await bot.polling(none_stop=True, timeout=60)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
