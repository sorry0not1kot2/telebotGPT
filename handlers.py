# файл handlers.py
import g4f
import translations
import logging

# Функция для обработки текстовых сообщений
async def handle_text(bot, message):
    query = message.text  # Получаем текст сообщения от пользователя
    try:
        # Отправляем запрос к GPT-4 для получения ответа
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4o",
            messages=[{"role": "user", "content": query}],
        )
       
        # Отправляем ответ пользователю с парсингом Markdown V1
        await bot.send_message(message.chat.id, response, parse_mode='Markdown')
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения: {e}")
        # Отправляем сообщение об ошибке, если произошла исключительная ситуация
        await bot.send_message(message.chat.id, f"{translations['error']}{str(e)}", parse_mode='Markdown')
