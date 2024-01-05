import asyncio
import settings

import openai
from openai.types import Completion

client = openai.AsyncOpenAI(
    api_key=settings.gpt_apikey,
    base_url=settings.gpt_server
)

async def create_req() -> Completion:
    return await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )

async def test():
    completion = await create_req()
    print(completion)
    print("```")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    print("hello?")
    asyncio.run(test())
