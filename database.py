import sqlite3
import sys
from typing import Tuple

con = sqlite3.connect("predlozhka.db")

con.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        message_id INTEGER PRIMARY KEY,
        file_id TEXT UNIQUE
    )
""")

if "user_data" not in con.execute("SELECT name FROM sqlite_master").fetchone():
    sys.exit("table not created")


def save_user_data(data: Tuple[int, str]) -> None:
    con.execute("INSERT INTO user_data VALUES (?, ?)", data)
    con.commit()


def get_file_id(msg_id: int) -> str:
    return con.execute("SELECT file_id FROM user_data WHERE message_id = ?", (msg_id,)).fetchone()[0]


def delete_user_data(msg_id: int) -> None:
    con.execute("DELETE FROM user_data WHERE message_id = ?", (msg_id,))
    con.commit()
