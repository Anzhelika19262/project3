import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Map_pt(SqlAlchemyBase, UserMixin):
    __tablename__ = 'map_pt'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    coord_pt = sqlalchemy.Column(sqlalchemy.String, nullable=True)