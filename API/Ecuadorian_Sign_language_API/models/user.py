from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Numeric, Float
from config.db import meta, engine

users = Table("users", meta, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255))
)

palabra = Table("palabra", meta,
    Column("id_palabra", Integer, primary_key=True, autoincrement=True),
    Column("palabra", String(100), nullable=False),
    Column("descripcion", String(200), nullable=False),
    Column("video", String(200), nullable=False)
)

caracter = Table("caracter", meta,
    Column("id_caracter", Integer, primary_key=True, autoincrement=True),
    Column("caracter", String(2), nullable=False),
    Column("video", String(200), nullable=False)
)

meta.create_all(engine)
