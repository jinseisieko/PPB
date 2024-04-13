import random

from discord import Embed, Color

import log_functions
from data import db_session

import discord
from discord.ext import commands
from config import config


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        log_functions.log_information("Bot Is Ready!!!")
        user = await bot.fetch_user(config['user_id'])
        embed = Embed(title="Bot Is Ready!!!", colour=Color.from_rgb(0, 255, 0))

        await user.send(embed=embed)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

        def check(m):
            return m.author.id == ctx.author.id

        answer = await bot.wait_for('message', check=check)
        answer = answer.content
        if answer == "aboba":
            await ctx.channel.send(':)')

    @bot.command(name="coin")
    async def heads_or_tails(ctx):
        def check(m):
            return m.author.id == ctx.author.id

        while True:
            tmp = Embed(title="Подбрасываю монетку!", colour=Color.from_rgb(0, 255, 0))
            tmp.set_image(url=
                          "https://cdn.discordapp.com/attachments/1227605957086019615/1228682002308399164/-50.gif?ex=662cee49&is=661a7949&hm=d69f16298361988d3840daf2f7e9349edcc33f6bd1d4d22b9eddfd9b9ce8833c&")

            await ctx.send(embed=tmp)
            await ctx.send(embed=Embed(title="Как думаешь, что выпало?", colour=Color.from_rgb(0, 255, 0)))

            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            dct = {0: "решка", 1: "орел"}
            real_result = dct[random.randint(0, 1)]
            if real_result in answer.lower():
                await ctx.channel.send('ПОБЕДА ПОСЛЕ ОБЕДА!!!1!!1!!1!!1!!111!1!!')
            else:
                await ctx.channel.send('ЖЕЕЕЕЕСТЬ! ТАКОГО ЛОХА ЕЩЕ ПОИСКАТЬ НАДО! АХАХАХАХААХАХ!!!!!!11!!1!1!')
            await ctx.channel.send('Хотите еще раз проигр... Попытать свою удачу, конечно?')
            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            if "нет" in answer.lower():
                break

    bot.run(config['token'])


if __name__ == '__main__':
    log_functions.log_information("Start main.py")
    db_session.global_init("db/PPB.db")

    main()
