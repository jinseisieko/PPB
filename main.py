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
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        answer = await bot.wait_for('message', check=check)
        answer = answer.content
        if answer == "aboba":
            await ctx.channel.send(':)')

    @bot.command(name="coin")
    async def heads_or_tails(ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        while True:
            tmp = Embed(title="Подбрасываю монетку!", colour=Color.from_rgb(255, 215, 0))
            tmp.set_image(url=
                          "https://cdn.discordapp.com/attachments/1227605957086019615/1228682002308399164/-50.gif?ex=662cee49&is=661a7949&hm=d69f16298361988d3840daf2f7e9349edcc33f6bd1d4d22b9eddfd9b9ce8833c&")

            await ctx.send(embed=tmp)
            await ctx.send(embed=Embed(title="Как думаешь, что выпало?\n"
                                             "1. Решка\n"
                                             "2. Орел\n"
                                             "Напиши цифру и свою ставку через пробел!",
                                       colour=Color.from_rgb(255, 215, 0)))

            while True:
                try:
                    answer = await bot.wait_for('message', check=check)
                    answer = answer.content
                    real_result = random.randint(1, 2)
                    if real_result == int(answer.split()[0]):
                        await ctx.channel.send(f'Действительно, ты прав!\n +{int(answer.split()[1])} points!')
                    elif real_result != int(answer.split()[0]) and int(answer.split()[0]) in [1, 2]:
                        await ctx.channel.send(f'Нет, ты не угадал!\n -{int(answer.split()[1])} points!')
                    else:
                        await ctx.channel.send('Я не понимаю. Введи только нужную цифру')
                        continue
                    break
                except Exception:
                    await ctx.channel.send('Я не понимаю. Введи только нужную цифру')
                    continue

            await ctx.channel.send(embed=Embed(title="Хочешь еще раз сыграть?\n"
                                                     "1. Да\n", colour=Color.from_rgb(255, 215, 0)))
            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            try:
                if 1 == int(answer.split()[0]):
                    continue
            except Exception:
                break
            break

    @bot.command(name="test")
    async def test(ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        tmp = Embed(title="test", colour=Color.from_rgb(255, 215, 0))
        tmp.set_image(url=
                      "https://cdn.discordapp.com/attachments/1178308857999654983/1229022138569195590/image.png?ex=662e2b0f&is=661bb60f&hm=3ef7638013c2b4cc80819b6bfe7bbed9535eacbb6e03cd8bcefc4bfaa08ef1ea&")

        await ctx.send(embed=tmp)

    bot.run(config['token'])


if __name__ == '__main__':
    log_functions.log_information("Start main.py")
    db_session.global_init("db/PPB.db")

    main()
