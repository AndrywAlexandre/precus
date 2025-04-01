from app.database import db

class usuario (db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    nome = db.column(db.string(250),nullable=False) # max de 250 caracteres e não vazio
    