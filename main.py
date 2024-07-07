import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
import handlers

# Настройка бота
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = AsyncTeleBot(BOT_TOKEN)

# Обработчик команды /start
async def start(message):
    await bot.send_message(message.chat.id, "Привет! Я бот на основе GPT-4. Спроси меня о чем угодно.")

# Добавление обработчиков
bot.register_message_handler(start, commands=['start'])
bot.register_message_handler(handlers.handle_text, content_types=['text'])

# Асинхронная функция main для запуска бота
async def main():
    await bot.polling(none_stop=True, timeout=60)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
