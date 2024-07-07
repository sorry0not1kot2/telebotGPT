import g4f
import translations

# Функция для обработки текстовых сообщений
async def handle_text(bot, message):
    query = message.text  # Получаем текст сообщения от пользователя
    try:
        # Отправляем запрос к GPT-4 для получения ответа
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4o",
            messages=[{"role": "user", "content": query}],
        )
        
        # Определяем тип данных ответа
        response_type = type(response).__name__
        
        # Проверяем, является ли ответ словарем и содержит ли он ключ 'choices'
        if isinstance(response, dict) and 'choices' in response and len(response['choices']) > 0:
            # Отправляем первый вариант ответа пользователю
            await bot.send_message(message.chat.id, response['choices'][0]['message']['content'])
        else:
            # Отправляем сообщение о некорректном ответе с указанием типа данных и самого ответа, отформатированного в Markdown
            await bot.send_message(message.chat.id, f"Некорректный ответ от GPT ({response_type}): ```{response}```", parse_mode='Markdown')
    except Exception as e:
        # Отправляем сообщение об ошибке, если произошла исключительная ситуация
        await bot.send_message(message.chat.id, f"{translations['error']}{str(e)}")
