from .user import User
from .db_session import create_session


async def registration_user(name, about, discord, ):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    if len(users) != 0:
        user = users[0]
        for user in users[1:]:
            db_sess.delete(user)
        return [user, False]

    user = User(name=name, about=about, discord=discord)
    db_sess.add(user)
    db_sess.commit()
    return [db_sess.query(User).where(User.discord == discord).first(), True]


async def profile_user(discord):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    user = users[0]
    for user in users[1:]:
        db_sess.delete(user)
    return user


async def check_(discord):
    db_sess = create_session()
    users = db_sess.query(User).where(User.discord == discord).all()
    if len(users) != 0:
        for user in users[1:]:
            db_sess.delete(user)
        return True
    else:
        return False
