"""USA Capital One debit bank statement."""

from datetime import datetime
from typing import Self

from usa_capital_one.capital_one_debit_statement_item import \
    CapitalOneDebitStatementItem
from utils.statement import Statement


class CapitalOneDebitStatement(Statement):
    """USA Capital One debit bank statement."""

    def __init__(self: Self, location: str) -> None:
        """
        Define the attributes of the statement and its location.

        :param location: Location of where the CSV file of the statement is.
        """
        super().__init__(location)
        self.table = "capital_one_debit"
        self.id_function = "get_capital_one_debit_transaction_id"
        self.attributes = (
            "transaction_id",
            "account_number",
            "transaction_date",
            "transaction_amount",
            "transaction_type",
            "transaction_description",
            "balance",
        )
        items = []

        for item in self.raw_items:
            items.append(
                CapitalOneDebitStatementItem(
                    int(item["account_number"]),
                    datetime.strptime(item["transaction_date"], "%m/%d/%y"),
                    float(item["transaction_amount"]),
                    item["transaction_type"],
                    item["transaction_description"],
                    float(item["balance"]),
                )
            )

        self.items = list(set(items))
