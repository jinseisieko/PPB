from .user import User
from .db_session import create_session


async def registration_user(name, about, discord, ):
    db_sess = create_session()
    if user := db_sess.query(User).where(User.discord == discord).first():
        return [user, False]

    user = User(name=name, about=about, discord=discord)
    db_sess.add(user)
    db_sess.commit()
    return [db_sess.query(User).where(User.discord == discord).first(), True]


async def profile_user(discord):
    db_sess = create_session()
    user = db_sess.query(User).where(User.discord == discord)
    return user


async def check_(discord):
    db_sess = create_session()
    if db_sess.query(User).where(User.discord == discord).first():
        return True
    else:
        return False
