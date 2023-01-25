"""Object to symbolize a generic bank statement."""

import csv
from typing import Self

from utils.sql_executioner import SqlExecutioner
from utils.statement_item import StatementItem


class Statement:
    """Object to symbolize a generic bank statement."""

    def __init__(self: Self, location: str) -> None:
        """
        Object to symbolize a generic bank statement.

        :param location: Location of where the CSV file of the statement is.
        """
        self.location = location
        self.raw_items = self.get_raw_items()
        self.items: list[StatementItem] = []
        self.table = ""
        self.id_function = ""
        self.attributes = ()

    def get_raw_items(self: Self) -> list:
        """
        Create the raw data from the statement file.

        :return: A list of dictionaries with the data from the statement.
        """
        all_items = []
        with open(self.location) as file:
            for i in csv.DictReader(file):
                item = {}
                for key, value in dict(i).items():
                    item[key.lower().replace(" ", "_")] = value
                all_items.append(item)

        return all_items

    def load_statement(self: Self, secret: dict) -> None:
        """
        Load all the items in the statement into a database.

        :param secret: Dictionary with credentials to the database.
        :return: None
        """
        executioner = SqlExecutioner(
            secret["username"],
            secret["password"],
            secret["host"],
            secret["port"],
            secret["db_name"],
        )
        for item in self.items:
            executioner.execute(
                item.get_insert(self.attributes, self.table, self.id_function)
            )

        executioner.cursor.connection.commit()
