TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read()

URI_INFO = f"https://api.telegram.org/bot{TOKEN}/getFile?file_id="
URI = f"https://api.telegram.org/file/bot{TOKEN}/"
