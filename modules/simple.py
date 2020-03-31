"""
A simple example module.
"""

from discord.ext import commands

class SimpleModule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('pong')


def setup(client):
    client.add_cog(SimpleModule(client))
