import sqlite3
from discord.ext import commands
import discord

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, region TEXT, ign TEXT)''')
        print('Register cog loaded')

    @commands.command(aliases=['register'])
    async def reg(self, ctx):
        self.c.execute('SELECT * FROM users WHERE id=?', (ctx.author.id,))
        data = self.c.fetchone()
        if data is not None:
            await ctx.send('You are already registered. Do you want to update your information? (yes/no)')
            update = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            if update.content.lower() != 'yes':
                await ctx.send('Cancelled.')
                return

        await ctx.send(f'Enter your region:')
        region = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        await ctx.send(f'Enter your IGN:')
        ign = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

        if data is not None:
            self.c.execute('UPDATE users SET region=?, ign=? WHERE id=?', (region.content, ign.content, ctx.author.id))
        else:
            self.c.execute('INSERT INTO users VALUES (?, ?, ?)', (ctx.author.id, region.content, ign.content))

        self.conn.commit()

        await ctx.send(f'You are from {region.content} and your IGN is {ign.content}.')

async def setup(bot):
    await bot.add_cog(Register(bot))