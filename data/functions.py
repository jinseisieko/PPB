from .user import User
from .friends import Friends
from .db_session import create_session


async def registration_user(name, about, discord, ):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    if len(users) != 0:
        user = users[0]
        for user in users[1:]:
            db_sess.delete(user)
        db_sess.commit()
        return [user, False]

    user = User(name=name, about=about, discord=discord)
    db_sess.add(user)
    db_sess.commit()


async def profile_user(discord):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    for user in users[1:]:
        db_sess.delete(user)
        db_sess.commit()
    db_sess = create_session()
    user = db_sess.query(User).where(User.discord == discord).first()
    return user


async def check_(discord):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    if len(users) != 0:
        for user in users[1:]:
            db_sess.delete(user)
        db_sess.commit()
        return True
    else:
        return False


async def delete_user(discord):
    db_sess = create_session()
    for user in db_sess.query(User).where(User.discord == discord).all():
        db_sess.delete(user)
    db_sess.commit()


async def is_friend(id_user, id_friend):
    db_sess = create_session()
    friends = db_sess.query(Friends).where(Friends.user_id == id_user).where(
                Friends.friend_id == id_friend).all()
    if len(friends) != 0:
        for friend in friends[1:]:
            db_sess.delete(friend)
        db_sess.commit()
        return True
    else:
        return False


async def add_friend(id_user, id_friend):
    if not await is_friend(id_user, id_friend):
        db_sess = create_session()
        friends = Friends()
        friends.user_id = id_user
        friends.friend_id = id_friend
        db_sess.add(friends)
        db_sess.commit()


async def del_friend(id_user, id_friend):
    if await is_friend(id_user, id_friend):
        db_sess = create_session()
        for friend in db_sess.query(Friends).where(Friends.user_id == id_user).where(
                Friends.friend_id == id_friend).all():
            db_sess.delete(friend)
        db_sess.commit()
