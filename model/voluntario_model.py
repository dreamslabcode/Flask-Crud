from helpers.database import db
from flask_restful import fields
from sqlalchemy.types import String

voluntario_fields = {
    'id_parceiro': fields.Integer(attribute='id_voluntario'),
    'nome': fields.String(attribute='nome'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone'),
    'stack': fields.String(attribute='stack'),
    'nivel_carreira': fields.String(attribute='nivel_carreira'),
    'tipo_pessoa': fields.String(attribute='tipo_pessoa')
}

class Voluntario(db.Model):

    __tablename__ = "tb_voluntario"
    __mapper_args__ = {'polymorphic_identity': 'voluntario' }
    
    id_voluntario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    stack = db.Column(db.String(200), nullable=False)
    nivel_carreira = db.Column(db.String(50), nullable=False)


    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id_pessoa"))
    tipo_pessoa = db.Column('tipo_pessoa', String(50), default='voluntario')

    def __init__(self, nome, email, telefone, stack, nivel_carreira):
        super().__init__(nome, email, telefone)
        self.nome = nome
        self.email = email
        self.stack = stack
        self.nivel_carreira = nivel_carreira

    def __repr__(self):
        return f'Voluntário(Nome={self.nome}, E-mail={self.email}, Stack={self.stack}, Nível de carreira={self.nivel_carreira})'