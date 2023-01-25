"""Object to assist in the execution of queries."""

from typing import Self

import pg8000


class SqlExecutioner:
    """Object to assist in the execution of queries."""

    def __init__(
        self: Self, username: str, password: str, host: str, port: int, db_name: str
    ) -> None:
        """
        Create a cursor when the object is instantiated.

        :param username: Username to connect to the database.
        :param password: Password to connect to the database.
        :param host: Hostname of the database.
        :param port: Port of the database.
        :param db_name: Name of the database.
        """
        self.cursor = pg8000.connect(
            database=db_name,
            user=username,
            password=password,
            host=host,
            port=port,
        ).cursor()

    def execute(self: Self, query: str) -> None:
        """
        Execute a query through the cursor.

        :param query: SQL to execute.
        :return: None
        """
        print(f"Executing -> {query}")
        self.cursor.execute(query)
