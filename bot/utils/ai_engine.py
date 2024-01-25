import openai
from bot.core.config import settings


client = openai.OpenAI(api_key=settings.api_key)


async def generate_ai(message):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты работник книжного магазина"},
                {"role": "user", "content": message},
            ],
            temperature=0.7,
            max_tokens=64,
            top_p=1,
        )
        print(response)
        return response.choices[0].message.content

    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)
        print("A 429 status code was received; we should back off a bit.")
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)
