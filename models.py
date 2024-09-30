# models.py
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    guess_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'