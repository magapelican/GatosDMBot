import sqlite3
import sys

con = sqlite3.connect("predlozhka.db")

con.execute("CREATE TABLE user_data(message_id, file_id)")

if "user_data" not in con.execute("SELECT name FROM sqlite_master").fetchone():
    sys.exit("table not created")

