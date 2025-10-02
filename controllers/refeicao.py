from database import db
from datetime import datetime

class RefeicaoController(db.Model):
    __tablename__ = 'refeicoes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    esta_na_receita = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'data_hora': self.data_hora.isoformat() if self.data_hora else None,
            'esta_na_receita': self.esta_na_receita
        }