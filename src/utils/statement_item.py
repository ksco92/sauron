"""Object to symbolize a generic line item in a bank statement."""

from typing import Self


class StatementItem:
    """Object to symbolize a generic line item in a bank statement."""

    def __eq__(self: Self, other: object) -> bool:
        """
        Equality is defined if all variables in the objects are equal.

        :param other: Object to compare to.
        :return: Whether the objects are equal or not.
        """
        if not isinstance(other, StatementItem):
            return NotImplemented

        return self.as_dict() == other.as_dict()

    def __str__(self: Self) -> str:
        """Representation is a dictionary with all the variables."""
        return str(vars(self))

    def __hash__(self: Self) -> int:
        """Hash is determined from all the attributes of the object."""
        return hash(str(self.as_dict()))

    def as_dict(self: Self) -> dict:
        """Return all the attributes as a dictionary."""
        return vars(self)

    def get_insert(
        self: Self,
        attribute_names: tuple,
        table_name: str,
        transaction_id_function_name: str,
    ) -> str:
        """
        Generate an insert statement for the statement item.

        :param attribute_names: Names of the attributes of the statement.
        :param table_name: Table to insert the item into.
        :param transaction_id_function_name: Name of the function that generates the transaction id.
        :return: An insert statement for the item.
        """
        f_name = transaction_id_function_name
        sep = "','"
        return (
            f"insert into sauron.{table_name} ({','.join(attribute_names)}) "
            f"values ({f_name}('{sep.join([str(v) for v in self.as_dict().values()])}'), "
            f"'{sep.join([str(v) for v in self.as_dict().values()])}'"
            f") on conflict do nothing;"
        )
