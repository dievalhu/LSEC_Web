from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from config.conexion import Conexion

conexion = Conexion()

DATABASE_URL = f"mysql://{conexion.user}:{conexion.pwd}@{conexion.host}/{conexion.db_name}"

engine = create_engine(DATABASE_URL)
meta = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
