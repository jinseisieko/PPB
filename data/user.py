import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    discord = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, unique=True)

    games = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    wins = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    coin_toss_games = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    coin_toss_wins = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    city_games = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    city_wins = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    city_record = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    city_avg_duration = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    points = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
