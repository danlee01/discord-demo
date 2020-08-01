import discord
from discord.ext import commands

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Command Success, Error, and Invocation Handler
    '''

    #we really only need this function, can put in main later as @bot.event
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + ' was invoked incorrectly.')
        print(error)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + ' was invoked successfully!')

def setup(bot):
    bot.add_cog(CommandEvents(bot))