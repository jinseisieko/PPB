from discord import Embed, Color


class Embeds:
    @staticmethod
    def on_ready():
        return Embed(title="Bot Is Ready!!!", colour=Color.from_rgb(0, 255, 0))

    @staticmethod
    def check_user():
        return Embed(title="Вы не зарегистрированы!",
                     description="Чтобы пользоваться командами вам необходимо зарегистрироваться\n"
                                 "`.registration` - напиши эту команду!",
                     color=Color.from_rgb(255, 0, 0))

    @staticmethod
    def registration(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Вы зарегистрированы!",
                         description="Чтобы в этом убедиться введите команду\n"
                                     "```.profile```",
                         color=Color.from_rgb(255, 0, 0))
        elif number == 1:
            return Embed(title="Регистрация",
                         description="Первым делом надо ввести имя :)\n"
                                     "**Выбирай с умом, потому что его сможет посмотреть любой пользователь!**",
                         colour=Color.from_rgb(0, 255, 0))
        elif number == 2:
            return Embed(title="Регистрация",
                         description=f"Ваше отображаемое имя: ***{kwargs['name']}***\n"
                                     f"Введите статус (расскажите немного о себе)",
                         colour=Color.from_rgb(0, 255, 0))
        elif number == 3:
            return Embed(title="Регистрация",
                         description=f"Ваш статус:\n"
                                     f"***{kwargs['about']}***\n"
                                     f"Регистрация закончена!\n"
                                     f"Чтобы в этом убедиться введите команду\n"
                                     "```.profile```",
                         colour=Color.from_rgb(0, 255, 0))

    @staticmethod
    def profile(*args, **kwargs):
        return Embed(title="Твой профиль",
                     description=f"Имя:\t\t**{kwargs['user'].name}**\n"
                                 f"Статус:\t\t**{kwargs['user'].about}**\n"
                                 f"Всего игр:\t\t**{kwargs['user'].games}**\n"
                                 f"Всего побед:\t\t**{kwargs['user'].wins}**\n"
                                 f"Очков на счету:\t\t**{kwargs['user'].points}**\n"
                                 f"Игр в **coin**:\t\t**{kwargs['user'].coin_toss_games}**\n"
                                 f"Побед в **coin**:\t\t**{kwargs['user'].coin_toss_wins}**\n"
                                 f"Игр в **cities**:\t\t**{kwargs['user'].city_games}**\n"
                                 f"Рекорд в **cities**:\t\t**{kwargs['user'].city_games}**\n"
                                 f"Средняя продолжительность в **cities**:\t\t**{kwargs['user'].city_avg_duration}**\n"
                                 f"Побед в **cities**:\t\t**{kwargs['user'].city_wins}**",
                     color=Color.from_rgb(0, 255, 0))

    @staticmethod
    def profile_by_id(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Профиль не найден!",
                         description=f"По id `{kwargs['id']}` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))
        if number == 1:
            return Embed(title="Твой профиль",
                         description=f"Имя:\t\t**{kwargs['user'].name}**\n"
                                     f"Статус:\t\t**{kwargs['user'].about}**\n"
                                     f"Всего игр:\t\t**{kwargs['user'].games}**\n"
                                     f"Всего побед:\t\t**{kwargs['user'].wins}**\n"
                                     f"Очков на счету:\t\t**{kwargs['user'].points}**\n"
                                     f"Игр в **coin**:\t\t**{kwargs['user'].coin_toss_games}**\n"
                                     f"Побед в **coin**:\t\t**{kwargs['user'].coin_toss_wins}**\n"
                                     f"Игр в **cities**:\t\t**{kwargs['user'].city_games}**\n"
                                     f"Рекорд в **cities**:\t\t**{kwargs['user'].city_games}**\n"
                                     f"Средняя продолжительность в **cities**:\t\t**{kwargs['user'].city_avg_duration}**\n"
                                     f"Побед в **cities**:\t\t**{kwargs['user'].city_wins}**",
                         color=Color.from_rgb(0, 255, 0))
    @staticmethod
    def delete_profile(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Удаление профиля",
                         description=f"Вы действительно хотите удалить профиль **{kwargs['name']}**,\n"
                                     f"Введите: `ДА`, чтобы удалить!",
                         color=Color.from_rgb(255, 0, 0))
        if number == 1:
            return Embed(title="Удаление профиля",
                         description=f"Профиль **{kwargs['name']}** удален",
                         color=Color.from_rgb(0, 255, 0), )

    @staticmethod
    def add_friend_by_id(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Профиль не найден!",
                         description=f"По id `{kwargs['id']}` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))
        if number == 1:
            return Embed(title="Заявка в друзья",
                         description=f"Пользователь под ником {kwargs['name']} отправил вам заявку в друзья\n"
                                     f"Напишите `ДА`, чтобы принять!",
                         color=Color.from_rgb(0, 255, 0))
        if number == 2:
            return Embed(title="Заявка в друзья",
                         description=f"Пользователь под ником {kwargs['name']} принял вашу заявку в друзья",
                         color=Color.from_rgb(0, 255, 0))
        if number == 3:
            return Embed(title="Заявка в друзья",
                         description=f"Вы успешно приняли заявку в друзья!",
                         color=Color.from_rgb(0, 255, 0))

    @staticmethod
    def is_friend_by_id(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Профиль не найден!",
                         description=f"По id `{kwargs['id']}` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))

        if number == 1:
            return Embed(title="Вы в друзьях",
                         description=f"Пользователь под ником {kwargs['name']} ваш друг!",
                         color=Color.from_rgb(0, 255, 0))

        if number == 2:
            return Embed(title="Вы НЕ в друзьях",
                         description=f"Пользователь под ником {kwargs['name']} НЕ ваш друг!",
                         color=Color.from_rgb(255, 0, 0))

    @staticmethod
    def del_friend_by_id(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Профиль не найден!",
                         description=f"По id `{kwargs['id']}` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))

        if number == 1:
            return Embed(title="Удалить друга",
                         description=f"Хотите сделать пользователя под ником {kwargs['name']} НЕ вашим другом!\n"
                                     f"Напишите `ДА`, чтобы принять!")

        if number == 2:
            return Embed(title="Удалить друга",
                         description=f"Пользователь под ником {kwargs['name']} НЕ ваш друг!",
                         color=Color.from_rgb(0, 255, 0))

    @staticmethod
    def coin_game(number, *args, **kwargs):
        if number == 0:
            tmp = Embed(title="Подбрасываю монетку!", colour=Color.from_rgb(255, 215, 0))
            tmp.set_image(url=
                          "https://cdn.discordapp.com/attachments/1227605957086019615/1228682002308399164/-50.gif?ex=662cee49&is=661a7949&hm=d69f16298361988d3840daf2f7e9349edcc33f6bd1d4d22b9eddfd9b9ce8833c&")
            return tmp
        if number == 1:
            return Embed(title="Как думаешь, что выпало?\n"
                               "1. Решка\n"
                               "2. Орел\n"
                               "Напиши цифру и свою ставку через пробел!",
                         colour=Color.from_rgb(255, 215, 0))
        if number == 2:
            return Embed(title="Хочешь еще раз сыграть?\n"
                               "1. Да\n", colour=Color.from_rgb(255, 215, 0))

    @staticmethod
    def cities_game(number, *args, **kwargs):
        game_color = "#2A32D4"
        if number == 0:
            tmp = Embed(title="Давай играть в города России!", colour=Color.from_str(game_color))
            tmp.set_image(url=
                          "https://media1.tenor.com/m/HWRcQJwQSjUAAAAC/cn-tower-toronto.gif")
            return tmp
        if number == 1:
            tmp = Embed(title="Правила игры такие:",
                        description="**Ты первый называешь любой существующий город России\n"
                                    "Затем каждый называет города на последнюю букву названного города\n"
                                    "Если таких нет - на букву раньше\n"
                                    "Не должно быть повторений городов\n"
                                    "Все названия в именительном падеже\n"
                                    "Если нет города ни на одну букву в названии, засчитывается поражение\n"
                                    "Три города, названных не по правилам - поражение\n"
                                    "Когда городов названо больше среднего, засчитвается победа**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 2:
            tmp = Embed(title=args[0], description=f"Этот город имеет население {args[1]['population']} чел.\n"
                                                   f"Расположен на территории этого субъекта: {args[1]['subject']}\n"
                                                   f"На координатах {args[1]['coords']['lat']}, {args[1]['coords']['lon']}\n"
                                                   f"[Читать на википедии](https://ru.wikipedia.org/wiki/{args[0].replace(' ', '_')})",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 3:
            tmp = Embed(title="Ой, кажется я не могу найти подходяший город! Похоже ты победил",
                        description=f"**Игра завершена со счётом: {args[0]}**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 4:
            tmp = Embed(title="Такого города в России нет!", description=f"**Осталось попыток: {3 - args[0]}**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 5:
            tmp = Embed(title=f"Название города начинается не на ту букву!\nНужна буква {args[0]}",
                        description=f"**Осталось попыток: {3 - args[1]}**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 6:
            tmp = Embed(title=f"Такой город уже был!\nНельзя снова использовать город {args[0]}",
                        description=f"**Осталось попыток: {3 - args[1]}**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 7:
            tmp = Embed(title="Игра сделала бум!",
                        description=f"**Игра завершена со счётом: {args[0]}**",
                        colour=Color.from_str(game_color))
            return tmp
        if number == 8:
            tmp = Embed(title=f"Ваш город - " + args[0], description=f"Этот город имеет население {args[1]['population']} чел.\n"
                                                   f"Расположен на территории этого субъекта: {args[1]['subject']}\n"
                                                   f"На координатах {args[1]['coords']['lat']}, {args[1]['coords']['lon']}\n"
                                                   f"[Читать на википедии](https://ru.wikipedia.org/wiki/{args[0].replace(' ', '_')})",
                        colour=Color.from_str(game_color))
            return tmp


class Messages:
    @staticmethod
    def coin_game(number, *args, **kwargs):
        if number == 0:
            return f'Действительно, ты прав!\n +{args[0][1]} points!'
        if number == 1:
            return f'Нет, ты не угадал!\n -{args[0][1]} points!'
        if number == 2:
            return 'Я не понимаю. Введи только то, что нужно'
