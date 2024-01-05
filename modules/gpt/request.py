import asyncio
import settings

from . import instruction
import openai
from openai.types import Completion

client = openai.AsyncOpenAI(
    api_key=settings.gpt_apikey,
    base_url=settings.gpt_server
)

async def create_req(prompt) -> Completion:
    return await client.chat.completions.create(
        model="gpt-3.5-turbo",
        timeout=60,
        messages=[
            {
                "role": "system",
                "content": instruction.python1,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

# Test
async def test():
    completion = await create_req("这句语句存在什么问题:print(\"Hello, world!)")
    print("```")
    print(completion.choices[0].message.content)
if __name__ == "__main__":
    asyncio.run(test())
