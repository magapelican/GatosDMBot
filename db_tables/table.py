import sys

class Table:

    def __init__(self, con, table_name, table_att1, table_att2) -> None:
        self.table_name = table_name
        self.table_att1 = table_att1
        self.table_att2 = table_att2
        self._con = con
        self._con.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                {self.table_att1},
                {self.table_att2}
            )
        """)

        if f"{table_name}" not in con.execute("SELECT name FROM sqlite_master").fetchone():
            sys.exit("table not created")

        
    def insert_data(self,data):
        self._con.execute(f"INSERT INTO {self.table_name} VALUES (?, ?)", data)
        self._con.commit()

    def delete_data_from_db(self,msg_id):
        self._con.execute(f"DELETE FROM {self.table_name} WHERE {self.table_att1} = ?", (msg_id,))
        self._con.commit()