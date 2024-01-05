import os
import asyncio

from ..mail import send
from ..mail import utils
from . import io
from ..gpt import request

async def create_task(msg, server):
    try:
        # Download the Zip file
        subject = utils.decode(msg.get('Subject'))
        await utils.download_attachment(msg, subject)
        print(f"Email {subject} processing...")

        homework_dir = './logs/homework/' + subject + '/'
        feedback_dir = './logs/feedback/' + subject + '/'

        # Try to decompress them(homework_dir), find all the .py file
        if not os.path.exists(homework_dir):
            raise Exception("未检查到你发送的附件")
        
        # await io.extract_files(homework_dir)
        py_files = []
        for root, dirs, files in os.walk(homework_dir):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(file)

        # Call the GPT, collect info and writing to the feedback_dir
        if not py_files:
            raise Exception("未检查到附件中的Python文件")

        if not os.path.exists(feedback_dir):
            os.makedirs(feedback_dir)
        print(f"in {subject}, {py_files}")
        for file in py_files:
            file_content = io.read_file(os.path.join(homework_dir, file))
            completion = await request.create_req(file_content)

            content = completion.choices[0].message.content
            target = os.path.join(feedback_dir, file.replace(".py", ".md"))

            io.write_file(target, content)
        
        # Send all content from GPT to the origin email.
        send.create_mail(
            server,
            msg.get('From'),
            "Re: "+subject,
            "some markdown lang"
        )
        await asyncio.sleep(3)
        print(f"{subject} Done")

    except Exception as e:
        print(f"Error while processing {utils.decode(msg.get('Subject'))}: {e}")
        send.create_mail(
            server,
            msg.get('From'),
            "(处理失败)Re: "+subject,
            f"同学, 你发送的邮件未被系统正确处理, 请检查后重新发送.\n可能的错误是: {e}"
        )