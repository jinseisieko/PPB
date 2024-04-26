import collections
import json
import random
import time

from discord import Embed, Color

import messages
from data import db_session
from data.functions import *
import discord
from discord.ext import commands
from config import config
import logging
from data.user import User
from messages import *


def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    async def check_valid_message(content):
        if content.startswith('.'):
            return False
        return True

    async def check_user(id_, message=True):
        if await check_(id_):
            return False
        else:
            if message:
                user = await bot.fetch_user(id_)
                await user.send(embed=Embeds.check_user())
            return True

    async def standard_answer(ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        answer = await bot.wait_for('message', check=check, timeout=30)
        answer = answer.content
        return answer

    @bot.event
    async def on_ready():
        logger.info("Bot Is Ready!!!")
        user = await bot.fetch_user(config['user_id'])
        await user.send(embed=Embeds.on_ready())

    @bot.command(name="registration")
    async def registration(ctx):
        if not await check_user(ctx.author.id, message=False):
            await ctx.send(embed=Embeds.registration(0))
            return

        await ctx.send(embed=Embeds.registration(1))

        name = await standard_answer(ctx)
        if not await check_valid_message(name):
            return
        await ctx.send(embed=Embeds.registration(2, name=name))

        about = await standard_answer(ctx)
        if not await check_valid_message(about):
            return

        await registration_user(name, about, ctx.author.id)
        await ctx.send(embed=Embeds.registration(3, about=about))

    @bot.command(name="profile")
    async def profile(ctx):
        if await check_user(ctx.author.id):
            return

        user: User = await profile_user(ctx.author.id)
        await ctx.send(embed=Embeds.profile(user=user))

    @bot.command(name="profile_by_id")
    async def profile_by_id(ctx, id_):
        if await check_user(ctx.author.id):
            return
        if await check_user(id_, message=False):
            await ctx.send(embed=Embeds.profile_by_id(0, id=id_))
            return

        user: User = await profile_user(id_)
        await ctx.send(embed=Embeds.profile_by_id(1, user=user))

    @bot.command(name="delete_profile")
    async def delete_profile(ctx):
        if await check_user(ctx.author.id):
            return
        user: User = await profile_user(ctx.author.id)
        await ctx.send(embed=Embeds.delete_profile(0, name=user.name))
        answer = await standard_answer(ctx)
        if answer == "ДА":
            await del_all_friends(user.id)
            await delete_user(ctx.author.id)
            await ctx.send(embed=Embeds.delete_profile(1, name=user.name))

    @bot.command(name="add_friend_by_id")
    async def add_friend_by_id(ctx, id_):
        """tu-turu"""
        if await check_user(ctx.author.id):
            return
        if await check_user(id_, message=False):
            await ctx.send(embed=Embeds.add_friend_by_id(0, id=id_))
            return

        user: User = await profile_user(ctx.author.id)
        friend: User = await profile_user(id_)

        d_user = await bot.fetch_user(user.discord)
        d_friend = await bot.fetch_user(friend.discord)
        await d_friend.send(embed=Embeds.add_friend_by_id(1, name=user.name))

        def check(m):
            return m.author.id == friend.discord and isinstance(m.channel, discord.channel.DMChannel)

        answer = await bot.wait_for('message', check=check)
        answer = answer.content
        if not await check_valid_message(answer):
            return

        if answer == "ДА":
            await add_friend(user.id, friend.id)
            await add_friend(friend.id, user.id)

            await d_friend.send(embed=Embeds.add_friend_by_id(3))
            await d_user.send(embed=Embeds.add_friend_by_id(2, name=friend.name))

    @bot.command(name="is_friend_by_id")
    async def is_friend_by_id(ctx, id_):
        if await check_user(ctx.author.id):
            return
        if await check_user(id_, message=False):
            await ctx.send(embed=Embeds.is_friend_by_id(0, id=id_))
            return

        user: User = await profile_user(ctx.author.id)
        friend: User = await profile_user(id_)

        if await is_friend(user.id, friend.id):
            await ctx.send(embed=Embeds.is_friend_by_id(1, name=friend.name))
        else:
            await ctx.send(embed=Embeds.is_friend_by_id(2, name=friend.name))

    @bot.command(name="del_friend_by_id")
    async def del_friend_by_id(ctx, id_):
        if await check_user(ctx.author.id):
            return
        if await check_user(id_, message=False):
            await ctx.send(embed=Embeds.del_friend_by_id(0, id=id_))
            return

        user: User = await profile_user(ctx.author.id)
        friend: User = await profile_user(id_)

        await ctx.send(embed=Embeds.del_friend_by_id(1, name=friend.name))
        answer = await standard_answer(ctx)
        if answer == "ДА":
            await del_friend(user.id, friend.id)
            await del_friend(friend.id, user.id)
            await ctx.send(embed=Embeds.del_friend_by_id(2, name=friend.name))

    @bot.command(name="ping")
    async def ping(ctx):
        if await check_user(ctx.author.id):
            return

        await ctx.send('pong')

    @bot.command(name="coin")
    async def heads_or_tails(ctx):
        if await check_user(ctx.author.id):
            return

        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        while True:
            await ctx.send(embed=messages.Embeds.coin_game(0))
            await ctx.send(embed=messages.Embeds.coin_game(1))

            while True:
                try:
                    answer = await bot.wait_for('message', check=check)
                    answer = answer.content
                    real_result = random.randint(1, 2)
                    answer = [int(answer.spit()[0]), check_points(ctx.author.id, int(answer.split()[1]))]
                    if real_result == answer[0]:
                        await ctx.channel.send(Messages.coin_game(0, answer))
                        await add_points(ctx.author.id, answer[1])
                        await coin_game(ctx.author.id, True)
                    elif real_result != answer[0] and answer[0] in [1, 2]:
                        await add_points(ctx.author.id, -answer[1])
                        await ctx.channel.send(Messages.coin_game(1, answer))
                        await coin_game(ctx.author.id, False)
                    else:
                        await ctx.channel.send(Messages.coin_game(2))
                        continue
                    break
                except Exception:
                    await ctx.channel.send(Messages.coin_game(2))
                    continue
            await ctx.channel.send(embed=Embeds.coin_game(2))
            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            try:
                if 1 == int(answer.split()[0]):
                    continue
            except Exception:
                break
            break

    @bot.command(name="cities")
    async def cities(ctx):
        if await check_user(ctx.author.id):
            return

        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        def check_rules(cities, was, previous, word):
            if word not in cities[1]:
                return 1
            if word in was:
                return 3
            if previous == "_":
                return 0
            try:
                previous = reversed(previous.upper())
                for x in previous:
                    if len(cities[0][x]) == 0:
                        continue
                    else:
                        for u in cities[0][x]:
                            if word == u["name"]:
                                del cities[0][x][cities[0][x].index(u)]
                                was.add(word)
                                return 0
                        else:
                            return 2
                return 2
            except Exception:
                return 1

        await ctx.send(embed=Embeds.cities_game(0))
        await ctx.send(embed=Embeds.cities_game(1))

        cities = json.load(open("resources/cities.json", "r", encoding="utf-8"))
        cities[0] = collections.defaultdict(lambda: "", cities[0])
        was = set()
        counter = 0
        score = 0
        previous = "_"

        while True:
            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            res = check_rules(cities, was, previous, answer)
            tmp_previous = answer
            # time.sleep(0)
            # res = 0
            # tmp_previous = previous
            if res == 0:
                previous = tmp_previous
                for x in reversed(previous.upper()):
                    if len(cities[0][x]) == 0:
                        continue
                    else:
                        city = random.choice(cities[0][x])
                        word = city['name']
                        was.add(word)
                        del cities[0][x][cities[0][x].index(city)]

                        await ctx.send(embed=Embeds.cities_game(2, word, city))
                        previous = word
                        break
                else:
                    await ctx.send(embed=Embeds.cities_game(3, score))
                    await add_points(ctx.author.id, int(score))
                    await cities_game(ctx.author.id, int(score))

                score += 1
            elif res == 1:
                counter += 1
                await ctx.send(embed=Embeds.cities_game(4, counter))
            elif res == 2:
                counter += 1
                need = ""
                for x in reversed(previous.upper()):
                    if len(cities[0][x]) == 0:
                        continue
                    else:
                        need = x.upper()
                        break
                await ctx.send(embed=Embeds.cities_game(5, need, counter))
            elif res == 3:
                counter += 1
                await ctx.send(embed=Embeds.cities_game(6, answer, counter))

            if counter == 3:
                await ctx.send(embed=Embeds.cities_game(7, score))
                await add_points(ctx.author.id, int(score))
                await cities_game(ctx.author.id, int(score))
                break

    bot.run(config['token'])


if __name__ == '__main__':
    db_session.global_init("db/PPB.db")
    main()
