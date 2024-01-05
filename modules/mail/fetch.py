import poplib
import datetime
from datetime import datetime

from . import utils

### Pop3 related
def connect_to_pop3(pop3_server, username, password):
    try:
        print("POP3 server...")
        server = poplib.POP3(pop3_server)
        server.user(username)
        server.pass_(password)
        print("has connected")
        return server
    except Exception as e:
        print(f"Error: POP3 server {e}")
        return None

def close_email_connection(server):
    try:
        print("POP3 server...")
        server.quit()
        print("has shutdown")
    except Exception as e:
        print(f"Error: POP3 server: {e}")

def fetch_emails(server, start_timestamp, end_timestamp):
    try:
        num_messages, _ = server.stat()
        print(f"Sum: {num_messages}")
        
        emails = []
        date_format = '%a, %d %b %Y %H:%M:%S %z'
        for i in range(num_messages, 0, -1):
            msg = utils.get_msg(server, i)
            msg_raw = msg.get('Date').split('(')[0].strip()
            msg_timestamp = datetime.strptime(msg_raw, date_format).timestamp()
            print(f"The {i} mail, message time: {msg_timestamp}")

            if msg_timestamp >= end_timestamp:
                continue
            if msg_timestamp <= start_timestamp:
                print("Fetching End")
                break
            emails.append(msg)
        return emails
    except Exception as e:
        print(f"Error while fetching emails: {e}")
        return None
    
# test
if __name__ == "__main__":
    import settings
    server = connect_to_pop3(settings.pop3_server, settings.username, settings.password)
    num_messages, total_size = server.stat()
    print(num_messages)

    msg = utils.get_msg(server, 1)
    msg_date = datetime.strptime(msg.get('Date'), '%a, %d %b %Y %H:%M:%S %z').timestamp()
    print(msg_date)

    current = datetime.now().timestamp()
    print(current)

    if(msg_date <= current):
        print("Yes")
    # download_attachment(msg)