"""USA Capital One debit bank statement item."""

import datetime
from typing import Self

from utils.statement_item import StatementItem


class CapitalOneDebitStatementItem(StatementItem):
    """USA Capital One debit bank statement item."""

    def __init__(
        self: Self,
        account_number: int,
        transaction_date: datetime.date,
        transaction_amount: float,
        transaction_type: str,
        transaction_description: str,
        balance: float,
    ) -> None:
        """
        Define the attributes of the statement item.

        :param account_number: Statement attribute.
        :param transaction_date: Statement attribute.
        :param transaction_amount: Statement attribute.
        :param transaction_type: Statement attribute.
        :param transaction_description: Statement attribute.
        :param balance: Statement attribute.
        """
        self.account_number = account_number
        self.transaction_date = transaction_date
        self.transaction_amount = transaction_amount
        self.transaction_type = transaction_type
        self.transaction_description = transaction_description
        self.balance = balance
