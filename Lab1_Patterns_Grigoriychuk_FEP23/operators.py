from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer


class Operator:
    def __init__(self, ID, talkingCharge, messageCost, networkCharge, discountRate):
        self.ID = ID
        self.talkingCharge = talkingCharge
        self.messageCost = messageCost
        self.networkCharge = networkCharge
        self.discountRate = discountRate

    def calculateTalkingCost(self, minute, customer):
        cost = minute * self.talkingCharge
        if customer.age < 18 or customer.age > 65:
            cost = cost * (1 - (self.discountRate / 100))
        return cost

    def calculateMessageCost(self, quantity, customer, other):
        cost = quantity * self.messageCost
        if customer.operators[0].ID == other.operators[0].ID:
            cost = cost * (1 - (self.discountRate / 100))
        return cost

    def calculateNetworkCost(self, amount):
        return amount * self.networkCharge
