import asyncio

from ..mail import utils

async def create_task(msg):
    try:
        subject = utils.decode(msg.get('Subject'))  
        await utils.download_attachment(msg, subject)
        await asyncio.sleep(3)
        print(f"{subject} Done")
    except Exception as e:
        print(f"Errow while processing: {e}")