TOKEN = None
ADMIN_ID = None

with open("token.txt") as f:
    TOKEN = f.read()

with open("admin_id.txt") as f:
    ADMIN_ID = f.read()

URI_INFO = f"https://api.telegram.org/bot{TOKEN}/getFile?file_id="
URI = f"https://api.telegram.org/file/bot{TOKEN}/"
