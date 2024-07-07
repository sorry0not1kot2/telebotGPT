import g4f
from telebot.async_telebot import AsyncTeleBot
import translations

async def handle_text(message):
    query = message.text
    try:
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4o",
            messages=[{"role": "user", "content": query}],
        )
        if isinstance(response, dict) and 'choices' in response and len(response['choices']) > 0:
            await bot.send_message(message.chat.id, response['choices'][0]['message']['content'])
        else:
            await bot.send_message(message.chat.id, "Некорректный ответ от GPT")
    except Exception as e:
        await bot.send_message(message.chat.id, f"{translations['error']}{str(e)}")

