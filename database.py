import sqlite3
from db_tables.user_data_table import User_data_table

con = sqlite3.connect("predlozhka.db")

user_data_table = User_data_table(
    con=con,
    table_name="user_data",
    table_att1="message_id",
    table_att2="file_id"
)

