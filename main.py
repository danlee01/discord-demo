import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='p!', descriptions='Pokedex')
bot.remove_command('help')
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
'''
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!dan'):
        await message.channel.send('a cutie')
'''
cogs = ['cogs.CommandEvents', 'cogs.helper', 'cogs.pokedex']
try:
    for cog in cogs:
        curr = cog
        bot.load_extension(cog)
except discord.ext.commands.errors.ExtensionAlreadyLoaded:
    bot.reload_extension(curr)

bot.run("your token here")