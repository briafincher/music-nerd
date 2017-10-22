from model2 import db, connect_to_db, app
from model2 import Artist

connect_to_db(app)

pop_index = db.Index('popularity_index', Artist.popularity)
engine = db.create_engine('postgresql:///music2')
pop_index.create(bind=engine)
db.session.commit()
