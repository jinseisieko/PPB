import collections
import json
import random

from discord import Embed, Color

from data import db_session
from data.functions import registration_user, check_, profile_user, delete_user

import discord
from discord.ext import commands
from config import config

import logging

from data.user import User
from messages import Embeds


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
    @discord.ext.commands.dm_only()
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
        if await check_user(id_, message=False):
            await ctx.send(embed=Embeds.profile_by_id(0, id=id_))
            return

        user: User = await profile_user(ctx.author.id)
        await ctx.send(embed=Embeds.profile_by_id(1, user=user))

    @bot.command(name="delete_profile")
    async def delete_profile(ctx):
        if await check_user(ctx.author.id):
            return
        user: User = await profile_user(ctx.author.id)
        await ctx.send(embed=Embeds.delete_profile(0, name=user.name))
        answer = await standard_answer(ctx)
        if answer == "ДА":
            await delete_user(ctx.author.id)
            await ctx.send(embed=Embeds.delete_profile(1, name=user.name))

    @bot.command(name="ping")
    async def ping(ctx):
        if await check_user(ctx.author.id):
            return

        await ctx.send('pong')

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

    @bot.command(name="cities")
    async def cities(ctx):
        game_color = "#2A32D4"

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

        tmp = Embed(title="Давай играть в города России!", colour=Color.from_str(game_color))
        tmp.set_image(url=
                      "https://media1.tenor.com/m/HWRcQJwQSjUAAAAC/cn-tower-toronto.gif")
        await ctx.send(embed=tmp)

        tmp = Embed(title="Правила игры такие:", description="**Ты первый называешь любой существующий город России\n"
                                                             "Затем каждый называет города на последнюю букву названного города\n"
                                                             "Если таких нет - на букву раньше\n"
                                                             "Не должно быть повторений городов\n"
                                                             "Все названия в именительном падеже\n"
                                                             "Если нет города ни на одну букву в названии, засчитывается поражение\n"
                                                             "Три города, названных не по правилам - поражение**",
                    colour=Color.from_str(game_color))
        await ctx.send(embed=tmp)

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
                        tmp = Embed(title=word, description=f"Этот город имеет население {city['population']} чел.\n"
                                                            f"Расположен на территории этого субъекта: {city['subject']}\n"
                                                            f"На координатах {city['coords']['lat']}, {city['coords']['lon']}\n"
                                                            f"[Читать на википедии](https://ru.wikipedia.org/wiki/{word.replace(' ', '_')})",
                                    colour=Color.from_str(game_color))
                        await ctx.send(embed=tmp)
                        previous = word
                        break
                else:
                    tmp = Embed(title="Ой, кажется я не могу найти подходяший город! Похоже ты победил",
                                description=f"**Игра завершена со счётом: {score}**",
                                colour=Color.from_str(game_color))
                    await ctx.send(embed=tmp)

                score += 1
            elif res == 1:
                counter += 1
                tmp = Embed(title="Такого города в России нет!", description=f"**Осталось попыток: {3 - counter}**",
                            colour=Color.from_str(game_color))
                await ctx.send(embed=tmp)
            elif res == 2:
                counter += 1
                need = ""
                for x in reversed(previous.upper()):
                    if len(cities[0][x]) == 0:
                        continue
                    else:
                        need = x.upper()
                tmp = Embed(title=f"Название города начинается не на ту букву!\nНужна буква {need}\n debug{previous}",
                            description=f"**Осталось попыток: {3 - counter}**",
                            colour=Color.from_str(game_color))
                await ctx.send(embed=tmp)
            elif res == 3:
                counter += 1
                tmp = Embed(title=f"Такой город уже был!\nНельзя снова использовать город {answer}",
                            description=f"**Осталось попыток: {3 - counter}**",
                            colour=Color.from_str(game_color))
                await ctx.send(embed=tmp)

            if counter == 3:
                tmp = Embed(title="Твоих знаний не достаточно, чтобы обыграть меня! Ты проиграл!",
                            description=f"**Игра завершена со счётом: {score}**",
                            colour=Color.from_str(game_color))
                await ctx.send(embed=tmp)
                break

    bot.run(config['token'])


if __name__ == '__main__':
    db_session.global_init("db/PPB.db")
    main()
