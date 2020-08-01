import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        help = "__**OPTIONS**__\n" \
               "prepend 'p!' to invoke commands.\n" \
               "**dex search [pokemon]** - Look up a pokemon's pokedex entry.\n" \
               "**dex randpoke**                  - Get a random pokedex entry."
        await ctx.send(help)

def setup(bot):
    bot.add_cog(Help(bot))