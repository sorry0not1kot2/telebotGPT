import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
import handlers

# Настройка бота
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = AsyncTeleBot(BOT_TOKEN)

# Обработчик команды /start
async def start(message):
    await bot.send_message(message.chat.id, "Привет! Я ботGPT-4. Слушаю тебя.")

# Добавление обработчиков
bot.register_message_handler(start, commands=['start'])
bot.register_message_handler(lambda message: handlers.handle_text(bot, message), content_types=['text'])

# Асинхронная функция main для запуска бота
async def main():
    await bot.polling(none_stop=True, timeout=60)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
