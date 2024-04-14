import collections
import json
import random
import time

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

        cities = json.load(open("data/cities.json", "r", encoding="utf-8"))
        cities[0] = collections.defaultdict(lambda: "", cities[0])
        was = set()
        counter = 0
        score = 0
        previous = "Лихославль"

        while True:
            answer = await bot.wait_for('message', check=check)
            answer = answer.content
            res = check_rules(cities, was, previous, answer)
            tmp_previous = answer
            # time.sleep(2)
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
    log_functions.log_information("Start main.py")
    db_session.global_init("db/PPB.db")

    main()
