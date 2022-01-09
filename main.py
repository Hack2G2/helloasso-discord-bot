#!/usr/bin/env python3
from utils.HelloAssoAPI import HelloAssoAPI

from os import getenv
from time import strftime

import asyncio
from aiohttp import web
from discord.ext import commands, tasks
import discord
import aiohttp
from dotenv import load_dotenv


bot = commands.Bot(command_prefix="!")


def print_log(msg):
    print(f"[{strftime('%d/%m/%Y - %H:%M:%S')}] {msg}")


async def print_send_log(msg, channel=None):
    print_log(msg)
    await channel.send(f"[{strftime('%d/%m/%Y - %H:%M:%S')}] {msg}")


@bot.event
async def on_ready():
    print_log("Bot is ready !")


@bot.command(name="members", help="Show all members.")
@commands.has_any_role("Bureau")
async def members(ctx):
    await print_send_log(f"Fetching members ...", channel=ctx.channel)
    orders = helloAssoAPI.get_form_orders(formSlug="cotisation-adhesion-2021-2022")
    for order in orders:
        await print_send_log(
            f"ID: {order.id}, Discord: {order.discord}", channel=ctx.channel
        )
    await print_send_log(f"We have {len(orders)} members !", channel=ctx.channel)


@members.error
async def members_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await print_send_log(
            f"Sorry {ctx.author.name}, you do not have permissions to do that!",
            channel=ctx.channel,
        )


class Webserver(commands.Cog):
    def __init__(self, client, host, port):
        self.client = client
        self.web_server.start()

        @routes.post("/" + SECRET_PATH)
        async def webhook(request):
            req_json = await request.json()
            if "payer" in req_json["data"]:
                order_id = req_json["data"]["items"][0]["payments"][0]["id"]
                order = helloAssoAPI.get_order_details(order_id)

                channel = client.get_channel(id=DISCORD_CHANNEL_ID)
                await channel.send(
                    f":new: A transaction has been made on helloasso ! (ID: {order.id}, Discord: {order.discord})"
                )

            return web.Response(text="Sucess !", content_type="text/html")

        app.add_routes(routes)

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=HOST, port=PORT)
        await site.start()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.client.wait_until_ready()


if __name__ == "__main__":
    load_dotenv()
    (
        HOST,
        PORT,
        DISCORD_TOKEN,
        DISCORD_CHANNEL_ID,
        SECRET_PATH,
        CLIENT_ID,
        CLIENT_SECRET,
    ) = (
        getenv("HOST"),
        getenv("PORT"),
        getenv("DISCORD_TOKEN"),
        int(getenv("DISCORD_CHANNEL_ID")),
        getenv("SECRET_PATH"),
        getenv("CLIENT_ID"),
        getenv("CLIENT_SECRET"),
    )

    app = web.Application()
    routes = web.RouteTableDef()
    helloAssoAPI = HelloAssoAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    bot.add_cog(Webserver(bot, HOST, PORT))
    print_log("Starting ...")
    bot.run(DISCORD_TOKEN)
