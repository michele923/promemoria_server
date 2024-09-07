from typing import List
import sqlite3


class serverDatabase:
    def _connect_check_tables(self, path: str) -> sqlite3.Connection:
        conn = sqlite3.connect(path)

        sql_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            {",".join(self.table_columns)}
        );
        """

        conn.execute(sql_query)
        conn.commit()

        return conn

    def __init__(self, db_path: str, table_name: str, id_col_name: str, title_col_name: str, desc_col_name: str, table_columns: List[str]) -> None:
        self.db_path = db_path
        self.table_name = table_name
        self.id_col_name = id_col_name
        self.title_col_name = title_col_name
        self.desc_col_name = desc_col_name
        self.table_columns = table_columns

    def get_posts(self):
        connection = self._connect_check_tables(self.db_path)

        connection.row_factory = sqlite3.Row
        posts = connection.execute(
            f"SELECT * FROM {self.table_name}").fetchall()

        connection.close()

        return posts

    def delete_post(self, id: int) -> None:
        connection = self._connect_check_tables(self.db_path)

        connection.row_factory = sqlite3.Row
        connection.execute(
            f"DELETE FROM {self.table_name} WHERE {self.id_col_name}=?", (id,))

        connection.commit()
        connection.close()

    def add_post(self, name: str, description: str) -> None:
        connection = self._connect_check_tables(self.db_path)

        connection.row_factory = sqlite3.Row
        connection.execute(f"INSERT INTO {self.table_name}({self.title_col_name}, {self.desc_col_name}) VALUES (?,?)",
                           (name, description))

        connection.commit()
        connection.close()
