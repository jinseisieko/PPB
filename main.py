from discord import Embed, Color

import log_functions
from data import db_session
from data.functions import registration_user, check_
from data.user import User

import discord
from discord.ext import commands
from config import config


async def check_user(discord, bot):
    if await check_(discord):
        print(123123)
        return False
    else:
        user = await bot.fetch_user(discord)
        embed = Embed(title="Регистрация!!!", colour=Color.from_rgb(0, 255, 0))
        await user.send(embed=embed)
        return True


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        # user = User(name="aboba")
        # user.discord = config["user_id"]
        # db_sess = db_session.create_session()
        #
        # db_sess.add(user)
        # db_sess.commit()

        log_functions.log_information("Bot Is Ready!!!")
        user = await bot.fetch_user(config['user_id'])
        embed = Embed(title="Bot Is Ready!!!", colour=Color.from_rgb(0, 255, 0))

        await user.send(embed=embed)

    @bot.command()
    @discord.ext.commands.dm_only()
    async def registration(ctx):
        if not await check_user(ctx.author.id, bot):
            embed = Embed(title="Вы зарегистрированы", colour=Color.from_rgb(0, 255, 0))
            await ctx.send(embed=embed)
            return

        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        embed = Embed(title="Начать регистрацию\nВведите отображаемое имя: ", colour=Color.from_rgb(0, 255, 0))
        await ctx.send(embed=embed)

        name = await bot.wait_for('message', check=check, timeout=30)
        name = name.content
        embed = Embed(title=f"Ваше отображаемое имя: {name}!\nВведите статус:", colour=Color.from_rgb(0, 255, 0))

        await ctx.send(embed=embed)

        about = await bot.wait_for('message', check=check, timeout=30)
        about = about.content
        embed = Embed(title=f"Ваш статус: {about}\nКонец Регистрации", colour=Color.from_rgb(0, 255, 0))
        await ctx.send(embed=embed)

        user, register_ = await registration_user(name, about, ctx.author.id)
        print(user.id, user.name, user.about, user.discord, register_)

    @bot.command()
    async def ping(ctx):
        if await check_user(ctx.author.id, bot):
            return

        await ctx.send('pong')

        def check(m):
            return m.author.id == ctx.author.id

        answer = await bot.wait_for('message', check=check)
        answer = answer.content
        if answer == "aboba":
            await ctx.channel.send(':)')

    bot.run(config['token'])


if __name__ == '__main__':
    log_functions.log_information("Start main.py")
    db_session.global_init("db/PPB.db")

    main()
