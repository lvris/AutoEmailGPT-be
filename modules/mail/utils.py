import os
import email
from email.message import Message

### Email processing related
def get_msg(server, index) -> Message:
    _, lines, _ = server.retr(index)
    bytes = b'\r\n'.join(lines)
    return email.message_from_bytes(bytes)

def decode(header: str):
    value, charset = email.header.decode_header(header)[0]
    if charset:
        return str(value, encoding=charset)
    else:
        return value

async def download_attachment(msg, foldername):
    for part in msg.walk(): 
        if part.get_content_disposition() == 'attachment':
            # Download
            attachment_name = decode(part.get_filename())
            attachment_content = part.get_payload(decode=True)  
            # Create
            attachment_folder = './logs/homework/' + foldername + '/'
            if not os.path.exists(attachment_folder):
                os.makedirs(attachment_folder)
            attachment_file = open(attachment_folder + attachment_name, 'wb')
            attachment_file.write(attachment_content) 
            attachment_file.close()