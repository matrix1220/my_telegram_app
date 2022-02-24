import Telegrambot

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker as sessionmkr
from sqlalchemy.ext.declarative import declarative_base

class Globals:
	bot = Telegrambot.bot("TOKEN")

	class db:
		engine = create_engine('sqlite:///datebase.db', echo=True)
		sessionmaker = sessionmkr(bind=engine)
		base = declarative_base()

		session = sessionmaker()
