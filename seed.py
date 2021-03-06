


""" seed some data into the database """
# from models import User, Word, db, connect_db
from user.user_model import db, connect_db, Word,User

from app import app

db.drop_all()
db.create_all()

# create a user
user = User.signup('testuser', 'testuserpassword','user.user@email.com', 'https://images.unsplash.com/photo-1586529726010-2411a6bec3c8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80' ,'male')
db.session.add(user)
db.session.commit()
# create a word
word = Word(word='blue', definition="of the color intermediate between green and violet; having a color similar to that of a clear unclouded sky",
part_of_speech='adjective', synonym="blueish", example="October's bright blue weather")
db.session.add(word)
user.words.append(word)
db.session.commit()

