import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite
sqlite_file_name = "database.sqlite"
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
engine = create_engine(database_url, connect_args={"check_same_thread": False})
Session = sessionmaker 
Base = declarative_base()


# MySQL
# URL_DB = "mysql+pymysql://root:root@localhost:3306/fastapi_db"
# engine = create_engine(URL_DB)
# Session = sessionmaker(autoflush=False, bind=engine)
# Base = declarative_base()

# postgresql
# URL_DB = "postgresql://root:root@localhost:5432/fastapi_db"
# engine = create_engine(URL_DB)
# Session = sessionmaker(autoflush=False, bind=engine)
# Base = declarative_base()

# mongodb
# URL_DB = "mongodb://localhost:27017"
# engine = create_engine(URL_DB)
# Session = sessionmaker(autoflush=False, bind=engine)
# Base = declarative_base()