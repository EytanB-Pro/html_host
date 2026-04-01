from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<User {self.name}>'
