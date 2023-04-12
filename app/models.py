# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class lab5(db.Model):

  __tablename__ = 'movies'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title= db.Column(db.String(80))
  description = db.Column(db.String(800))
  poster = db.Column(db.String(255))
  created_at = db.Column(db.DateTime())

  def __init__(self, title, description, poster):
    self.title=title
    self.description=description
    self.poster=poster
    self.created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 
