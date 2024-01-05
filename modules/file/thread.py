import os
import asyncio

from ..mail import send
from ..mail import utils
from . import extract
from ..gpt import request

async def create_task(msg):
    try:
        # Download the Zip file
        subject = utils.decode(msg.get('Subject'))
        await utils.download_attachment(msg, subject)

        homework_dir = './logs/homework/' + subject + '/'
        feedback_dir = './logs/feedback/' + subject + '/'

        # Try to decompress them(homework_dir), find all the .py file
        await extract.do(homework_dir)

        for root, dirs, files in os.walk():
            for file in files:
                if file.endswith(".py"):
                    py_file_path = os.path.join(root, file)
                    print(f"Found .py file: {py_file_path}")

        # Call the GPT, collect info and writing to the feedback_dir
        await request.create_req("Some .py explaination")

        # Send all content from GPT to the origin email.
        send.do(msg.get('From'), feedback_dir)

        await asyncio.sleep(3)
        print(f"{subject} Done")
    except Exception as e:
        print(f"Errow while processing: {e}")