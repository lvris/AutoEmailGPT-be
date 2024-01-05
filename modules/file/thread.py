import os
import asyncio

from ..mail import send
from ..mail import utils
from . import io
from ..gpt import request

async def create_task(msg):
    try:
        # Download the Zip file
        subject = utils.decode(msg.get('Subject'))
        await utils.download_attachment(msg, subject)
        print(f"Email {subject} processing...")

        homework_dir = './logs/homework/' + subject + '/'
        feedback_dir = './logs/feedback/' + subject + '/'

        # Try to decompress them(homework_dir), find all the .py file
        if os.path.exists(homework_dir):
            raise Exception("未检查到你发送的附件")
        
        await io.extract_files(homework_dir)
        py_files = []
        for root, dirs, files in os.walk(homework_dir):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))

        # Call the GPT, collect info and writing to the feedback_dir
        if not py_files:
            raise Exception("未检查到附件中的Python文件")

        print(f"in {subject}, {py_files}")
        for file in py_files:
            completion = await request.create_req(io.read_file(file))
        print(completion.choices[0].message.content)

        # Send all content from GPT to the origin email.
        # send.do(msg.get('From'), feedback_dir)

        await asyncio.sleep(3)
        print(f"{subject} Done")
    except Exception as e:
        print(f"Errow while processing {utils.decode(msg.get('Subject'))}: {e}")
        # Send Error Message to the origin emailbox too