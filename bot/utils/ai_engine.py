from openai import OpenAI

from bot.config_data.config_reader import settings
client = OpenAI(api_key=settings.api_token)


async def generate_ai(message):
    try:
        completion = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {'role': 'system', 'content': "Ты Петр Первый!"},
                {'role': 'user', 'content': message}],
        )
        print(completion['choices'][0]['message']['content'])
        return completion['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return None
