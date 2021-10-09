#!/usr/bin/env python3
from aiohttp import web
from discord.ext import commands, tasks
import discord
import aiohttp
from dotenv import load_dotenv
from os import getenv


class Webserver(commands.Cog):
    def __init__(self, client, host, port):
        self.client = client
        self.web_server.start()

        @routes.post("/" + SECRET_PATH)
        async def webhook(request):
            channel = client.get_channel(id=DISCORD_CHANNEL_ID)
            await channel.send(":new: A transaction has been made on helloasso !")
            
            return web.Response(text='Sucess !',content_type='text/html')

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
    HOST, PORT, DISCORD_TOKEN, DISCORD_CHANNEL_ID, SECRET_PATH = (
        getenv("HOST"),
        getenv("PORT"),
        getenv("DISCORD_TOKEN"),
        int(getenv("DISCORD_CHANNEL_ID")),
        getenv("SECRET_PATH"),
    )

    app = web.Application()
    routes = web.RouteTableDef()

    bot = commands.Bot(command_prefix="!")
    bot.add_cog(Webserver(bot, HOST, PORT))
    bot.run(DISCORD_TOKEN)
