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
        help = "__**OPTIONS**__\n" \
               "**search [pokemon]** - Look up a pokemon's pokedex entry.\n" \
               "**randpoke**                  - Get a random pokedex entry."

        await ctx.channel.send(help)

    @pokedex.command()
    async def search(self, ctx):
        """Sends a Pokedex entry to channel"""
        args = ctx.message.content.split()
        args.remove('p!dex')
        args.remove('search')
        try:
            pokemon = pb.pokemon(args[0])
        except ValueError:
            await ctx.send("```I couldn't find that entry!```")

        entry = create_entry(pokemon)
        await ctx.send(embed=entry)



    @pokedex.command()
    async def randpoke(self, ctx):
        """Sends a random Pokedex entry to channel"""
        entry = create_entry(pb.pokemon(random.randint(0,350)))
        await ctx.channel.send(embed=entry)


def setup(bot):
    bot.add_cog(Pokedex(bot))

def create_entry(pokemon):
    """Returns a formatted pokedex entry"""
    entry = discord.Embed(
        title=pokemon.name.capitalize(),
        description=f"*{pokemon.id}*",
        color=discord.Color.red()
    )

    #  The following ugly code is a workaround of a part of the pokebase module that don't work
    # sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon.id}.png"
    sprite_url = f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon.name}.gif"
    entry.set_image(url=sprite_url)
    SEPARATOR = ', '
    types = [field.type.name.capitalize() for field in pokemon.types]

    stats = f"__**Height:**__ {pokemon.height} \n__**Weight**__: {pokemon.weight}"
    entry.add_field(name='Base Stats', value=stats, inline=True)
    entry.add_field(name='Type', value=SEPARATOR.join(types), inline=True)

    return entry
