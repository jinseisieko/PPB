import os

import log_functions
from data import db_session

import discord
from discord.ext import commands
from dislash import InteractionClient



def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('MTIyNzU5MjU3MjIzNTQxNTU5Mg.GwHZrl.CFfnVkVhHpweL133vxEzRGugrxQNDy4uYSbqYo')


if __name__ == '__main__':
    intents = discord.Intents.default()
    db_session.global_init("db/PPB.db")
    log_functions.log_information("Start")
    main()
