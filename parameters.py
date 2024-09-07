from database import serverDatabase


class serverParameters:
    def __init__(self) -> None:

        # LOGIN

        self.USERNAME = 'user'
        self.PASSWORD = '1'

        # FLASK

        self.app_secret_key = '12345678'

        # DATABASE

        self.db_path = "files/db.sqlite"

        self.table_name = "posts"
        self.id_col_name = "id"
        self.title_col_name = "titolo"
        self.desc_col_name = "spiegazione"

        self.table_columns = [f"{self.id_col_name} INTEGER PRIMARY KEY AUTOINCREMENT",
                              f"{self.title_col_name} TEXT",
                              f"{self.desc_col_name} TEXT"]

        self.database = serverDatabase(self.db_path, self.table_name, self.id_col_name,
                                       self.title_col_name, self.desc_col_name, self.table_columns)


params = serverParameters()
