from database import db
class RefeicaoController(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    esta_na_receita = db.Column(db.Boolean, nullable=False)