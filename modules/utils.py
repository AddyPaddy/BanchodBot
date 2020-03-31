"""
A utility module.
"""

from discord.ext import commands

class UtilsModule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='hej')
    async def ping(self, ctx):
        await ctx.send('monika')


def setup(client):
    client.add_cog(UtilsModule(client))
