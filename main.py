# import settings

# from modules.mail import fetch
# from modules.mail import utils
# from modules.mail import send
# from modules.file import thread

# import re
# import asyncio
# import datetime
# from datetime import datetime

# # Get current time, read the time it runs before, write to the log file.
# with open('./logs/runtime/log.txt', 'r') as file:
#     lines = file.readlines()
#     last_timestamp = float(lines[-1] if lines else 1704000000)
# last_timestamp = 1704000000 ### Debug
# with open('./logs/runtime/log.txt', 'a') as file:
#     now_timestamp = datetime.now().timestamp()
#     file.writelines(str(now_timestamp)+'\n')

# # Fetch data, get an mail array
# server = fetch.connect_to_pop3(
#     settings.pop3_server, 
#     settings.username, 
#     settings.password
# )
# msgs = fetch.fetch_emails(server, last_timestamp, now_timestamp)
# fetch.close_email_connection(server)

# # Ready for sending emails
# server = send.connect_to_smtp(
#     settings.smtp_server, 
#     settings.smtp_port, 
#     settings.username, 
#     settings.password
# )

# # Filter the mail through regex, create thread respectively
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         for msg in msgs:
#             subject = utils.decode(msg.get('Subject'))  
#             if bool(re.match(settings.pattern, subject)):
#                 tg.create_task(thread.create_task(msg, server))
#     print("---Finished---")
#     server.quit()

# asyncio.run(main())
print("hello")