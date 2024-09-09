from database import serverDatabase
import json


class serverParameters:
    def __init__(self, config_file_path: str) -> None:

        with open(config_file_path) as config_file:
            config_json = json.load(config_file)

        # LOGIN
        _user_settings = config_json["USER"]

        self.USERNAME = _user_settings["USERNAME"]
        self.PASSWORD = _user_settings["PASSWORD"]

        # FLASK
        _flask_settings = config_json["FLASK"]

        self.app_secret_key = _flask_settings["app_secret_key"]

        # DATABASE
        _database_settings = config_json["DATABASE"]

        self.db_path = _database_settings["db_path"]

        self.table_name = _database_settings["table_name"]

        _columns_settings = _database_settings["columns"]

        self.id_col_name = _columns_settings["id"][0]
        self.title_col_name = _columns_settings["title"][0]
        self.desc_col_name = _columns_settings["description"][0]

        self.table_columns = [" ".join(_columns_settings["id"]),
                              " ".join(_columns_settings["title"]),
                              " ".join(_columns_settings["description"])]

        self.database = serverDatabase(self.db_path, self.table_name, self.id_col_name,
                                       self.title_col_name, self.desc_col_name, self.table_columns)


params = serverParameters("files/config.json")
