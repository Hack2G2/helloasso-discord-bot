#!/usr/bin/env python3


class Order:
    def __init__(self, orderId, email, firstName, lastName, discord):
        self.id = orderId
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.discord = discord
