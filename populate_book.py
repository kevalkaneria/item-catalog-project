from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import User, Genre, Base, BookItem

engine = create_engine('sqlite:///new_book_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
# the first user
User1 = User(name="Assiya Kh", email="assiyakhuzyakhmetova@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png')
session.add(User1)
session.commit()

# Poetry Books
genre1 = Genre(user_id=1, name="food", description = "sea food")

session.add(genre1)
session.commit()








print "DB is populated"
