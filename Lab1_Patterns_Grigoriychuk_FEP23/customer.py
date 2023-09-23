from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from operators import Operator


class Customer:
    def __init__(self, ID, name, age, operators, bills, limitingAmount):
        self.ID = ID
        self.name = name
        self.age = age
        self.operators = operators  # []
        self.bills = bills  # []

    def talk(self, minute, other):
        cost = self.operators[0].calculateTalkingCost(minute, self)
        self.bills[0].add(cost)

    def message(self, quantity, other):
        cost = self.operators[0].calculateMessageCost(quantity, self, other)
        self.bills[0].add(cost)

    def connection(self, amount):
        cost = self.operators[0].calculateNetworkCost(amount)
        self.bills[0].add(cost)
