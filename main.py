import sys, os
import traceback

import discord
from discord.ext import commands
from discord.ext.commands import bot

import constants

class BanchodBot():
    def __init__(self, client, constants):
        self.client = client
        self.constants = constants

        """Copied as is from discord.py docs"""
        if __name__ == '__main__':
            for module in self.constants.INIT_MODULES:
                try:
                    self.client.load_extension(module)
                    print("Loaded {}".format(module))
                except Exception as e:
                    print("Failed to load module {}".format(module))
                    traceback.print_exc()

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    @commands.command(name="load")
    async def load(self, ctx, module_name : str):
        """Loads a module."""
        try:
            self.client.load_extension(module_name)
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send("{} loaded.".format(module_name))

    @commands.command(name="unload")
    async def unload(self, ctx, module_name : str):
        """Unloads a module."""
        if module_name in self.constants.UTIL_MODULES:
            await ctx.send(f"{module_name} is a utility module. It cannot be unloaded.")

        self.client.unload_extension(module_name)
        await ctx.send(f"{module_name} unloaded.")

    @commands.command(name="shutdown")
    async def shutdown(self, ctx):
        """Shutdown command (need to add owner check)"""
        await self.client.logout()

    @commands.command(name="restart")
    async def restart(self, ctx):
        """Restart command (need to add owner check)"""
        self.restart_program()
        await self.client.close()

consts = constants.Constants()
client = commands.Bot(command_prefix=consts.BOT_PREFIX)

@client.event
async def on_ready():
    ready_message = "Logged in as " + client.user.name
    print(ready_message)

bot = BanchodBot(client, consts)

#client.run("authkeyhere")

