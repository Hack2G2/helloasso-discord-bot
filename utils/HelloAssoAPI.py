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

    def get_orders_at_page(
        self,
        organizationSlug="hack2g2",
        formType="Membership",
        formSlug="cotisation-adhesion-2021-2022",
        page=1,
    ):
        headers = {"Authorization": "Bearer " + self.access_token}
        req = get(
            f"https://api.helloasso.com/v5/organizations/{organizationSlug}/forms/{formType}/{formSlug}/items?tierTypes=Membership&withDetails=true&pageIndex={page}",
            headers=headers,
        )
        response = req.json()

        orders = []
        for data in response["data"]:
            order = Order(
                orderId=data["order"]["id"],
                email=data["payer"]["email"],
                firstName=data["payer"]["firstName"],
                lastName=data["payer"]["lastName"],
                discord=data["customFields"][1]["answer"],
            )
            orders.append(order)
        return orders

    def get_form_orders(
        self,
        organizationSlug="hack2g2",
        formType="Membership",
        formSlug="cotisation-adhesion-2021-2022",
    ):
        headers = {"Authorization": "Bearer " + self.access_token}
        req = get(
            f"https://api.helloasso.com/v5/organizations/{organizationSlug}/forms/{formType}/{formSlug}/items?tierTypes=Membership",
            headers=headers,
        )
        pagination = req.json()["pagination"]

        orders = []
        for i in range(1, pagination["totalPages"] + 1):
            orders += self.get_orders_at_page(
                organizationSlug, formType, formSlug, page=i
            )
        return orders
