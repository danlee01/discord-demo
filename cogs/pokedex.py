import discord
from discord.ext import commands
import pokebase as pb
import random
class Pokedex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='dex', invoke_without_command=True)
    async def pokedex(self, ctx):
        """Base command for Pokedex"""
        await ctx.channel.send("base pokedex cmd")

    @pokedex.command()
    async def search(self, ctx):
        """Returns a Pokedex entry"""
        args = ctx.message.content.split()
        args.remove('t!dex')
        args.remove('search')
        try:
            pokemon = pb.pokemon(args[0])
        except ValueError:
            await ctx.send("```I couldn't find that entry!```")

        entry = discord.Embed(
            title=pokemon.name,
            description='shit idk yet',
            color=discord.Color.red()
        )

        entry.set_image(url='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png')

        await ctx.send(embed=entry)



    @pokedex.command()
    async def randpoke(self, ctx):
        """Returns a random Pokedex entry"""
        await ctx.channel.send("```"+pb.pokemon(random.randint(0,350)).name+"```")


def setup(bot):
    bot.add_cog(Pokedex(bot))
