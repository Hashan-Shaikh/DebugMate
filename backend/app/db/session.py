from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Connection string: postgresql://<user>:<password>@<host>:<port>/<dbname>
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/chatbot_db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
