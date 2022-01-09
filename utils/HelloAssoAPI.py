#!/usr/bin/env python3
from utils.Order import Order
from requests import get, post


class HelloAssoAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.get_tokens()

    def get_tokens(self):
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }

        req = post("https://api.helloasso.com/oauth2/token", headers=headers, data=data)
        response = req.json()
        self.access_token = response["access_token"]
        self.refresh_token = response["refresh_token"]

    def get_order_details(self, order_id):
        headers = {"Authorization": "Bearer " + self.access_token}
        print("Order id :", order_id)
        req = get(
            f"https://api.helloasso.com/v5/items/{order_id}?withDetails=true",
            headers=headers,
        )
        response = req.json()

        order = Order(
            orderId=order_id,
            email=response["payer"]["email"],
            firstName=response["payer"]["firstName"],
            lastName=response["payer"]["lastName"],
            discord=response["customFields"][1]["answer"],
        )
        return order

    def get_form_orders(
        self,
        organizationSlug="hack2g2",
        formType="Membership",
        formSlug="cotisation-adhesion-2021-2022",
    ):
        headers = {"Authorization": "Bearer " + self.access_token}
        req = get(
            f"https://api.helloasso.com/v5/organizations/{organizationSlug}/forms/{formType}/{formSlug}/items",
            headers=headers,
        )
        response = req.json()

        for data in response["data"]:
            yield self.get_order_details(data["order"]["id"])
