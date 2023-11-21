from db_tables.table import Table

class User_data_table(Table):

    def __init__(self, con, table_name, table_att1, table_att2) -> None:
        super().__init__(con, table_name, table_att1, table_att2)

    def get_file_id(self,msg_id):
        return self._con.execute(f"SELECT file_id FROM {self.table_name} WHERE {self.table_att1} = ?", (msg_id,)).fetchone()[0]