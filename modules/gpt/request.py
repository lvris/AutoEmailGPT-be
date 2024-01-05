import asyncio
import settings

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
                "content": "现在你是一名PYTHON教师,请你根据以下的标准评估接下来作业的完整性、准确性和清晰度,并给出任何可能的改进建议:\n1.根据程序语法是否准确从1分到5分进行打分\n2.根据是否符合题目,是否准确完成要求要求从1分到5分进行打分\n3.根据解题思路是否有创造性从1分到5分进行打分",
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
