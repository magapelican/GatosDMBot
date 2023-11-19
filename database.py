import sqlite3
import sys

con = sqlite3.connect("predlozhka.db")

con.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        message_id,
        file_id
    )
""")

if "user_data" not in con.execute("SELECT name FROM sqlite_master").fetchone():
    sys.exit("table not created")


def insert_data(data):
    con.execute("INSERT INTO user_data VALUES (?, ?)", data)
    con.commit()


def get_file_id(msg_id):
    return con.execute("SELECT file_id FROM user_data WHERE message_id = ?", (msg_id,)).fetchone()[0]


def delete_data_from_db(msg_id):
    con.execute("DELETE FROM user_data WHERE message_id = ?", (msg_id,))
    con.commit()
