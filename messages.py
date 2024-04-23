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
                                 f"Статус:\t\t**{kwargs['user'].about}**\n",
                     color=Color.from_rgb(0, 255, 0))

    @staticmethod
    def profile_by_id(number, *args, **kwargs):
        if number == 0:
            return Embed(title="Профиль не найден!",
                         description=f"По id `{kwargs['id']}` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))
        if number == 1:
            return Embed(title="Профиль",
                         description=f"Имя:\t\t**{kwargs['user'].name}**\n"
                                     f"Статус:\t\t**{kwargs['user'].about}**\n",
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
