from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    user_id = db.Column(db.Int, primary_key = True),
    nombre = db.Column(db.Int, nullable=False)

class Reservacion(db.Model):
    reservacion_id = db.Column(db.Int, primary_key = True),
    nombre = db.Column(db.String(100), nullable=False),
    contacto = db.Column(db.String(100), nullable=False)
    cantidad_personas = db.Column(db.Int, nullable=False),
    fecha = db.Column(db.Date, nullable=False),
    hora = db.Column(db.Date, nullable=False)
