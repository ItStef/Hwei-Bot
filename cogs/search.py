from discord.ext import commands
import discord

class Search(commands.Cog):
    def __innit__(self, bot):
        self.bot = bot

    @commands.command(aliases=['search'])
    async def find(self, ctx, *, query):
        await ctx.send(f'You searched for {query}.')

async def setup(bot):
    await bot.add_cog(Search(bot))    
