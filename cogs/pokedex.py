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

        #  The following ugly code is a workaround of a part of the pokebase module that don't work
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon.id}.png"
        entry.set_image(url=sprite_url)
        SEPARATOR = ', '
        types = [field.type.name for field in pokemon.types]
        entry.add_field(name='Base Stats', value='stats go here', inline=True)
        entry.add_field(name='Type', value=SEPARATOR.join(types), inline=True)

        await ctx.send(embed=entry)



    @pokedex.command()
    async def randpoke(self, ctx):
        """Returns a random Pokedex entry"""
        await ctx.channel.send("```"+pb.pokemon(random.randint(0,350)).name+"```")


def setup(bot):
    bot.add_cog(Pokedex(bot))
