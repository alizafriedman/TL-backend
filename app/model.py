from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Form(db.Model):
    __tablename__ = 'forms'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(200), nullable=False)

