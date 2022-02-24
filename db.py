from config import Globals

db = Globals.db

from sqlalchemy import Column, Integer, String
class chats(db.base):
	__tablename__ = 'chats'

	id = Column(Integer, primary_key=True)
	type = Column(String)
	full_name = Column(String)
	username = Column(String)

	def __repr__(self):
		return "<chat(id='%i')>" % (self.id)

class messages(db.base):
	__tablename__ = 'messages'

	id = Column(Integer, primary_key=True)
	From = chats.id
	date = Column(Integer)
	full_name = Column(String)
	username = Column(String)

	def __repr__(self):
		return "<chat(id='%i')>" % (self.id)

db.base.metadata.create_all(db.engine)

# from sqlalchemy.orm import sessionmaker
# session = sessionmaker(bind=engine)()

#session = db.sessionmaker()
#print(session.query(User).filter(User.id==4).first())

# user = User(id=2, action=2)
# session.add(user)

# session.commit()

def UserId(id):
	user = db.session.query(User).filter(User.id==id).first()
	if user: return user
	else:
		user = User(id=id)
		db.session.add(user)
		return user