from discord import Embed, Color


class Embeds:
    @staticmethod
    def on_ready():
        return Embed(title="Bot Is Ready!!!", colour=Color.from_rgb(0, 255, 0))

    @staticmethod
    def check_user():
        return Embed(title="Вы не зарегистрированы!",
                     description="Чтобы пользоваться командами вам необходимо зарегистрироваться\n"
                                 "```.registration```\n"
                                 "Напиши эту команду мне в личные сообщения!",
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
                         description=f"По id ```{kwargs['id']}``` профиль не найден.\n"
                                     f"Видимо этот пользователь еще не создал профиль либо уже успел его удалить;)",
                         color=Color.from_rgb(255, 0, 0))
        if number == 1:
            return Embed(title="Профиль",
                         description=f"Имя:\t\t**{kwargs['user'].name}**\n"
                                     f"Статус:\t\t**{kwargs['user'].about}**\n",
                         color=Color.from_rgb(0, 255, 0))
