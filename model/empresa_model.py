from helpers.database import db
from flask_restful import fields

empresa_fields = {
    'id_empresa': fields.Integer(attribute='id_empresa'),
    'nome_fantasia': fields.String(attribute='nome_fantasia'),
    'cnpj': fields.String(attribute='cnpj'),
    'email': fields.String(attribute='cnpj'),
    'telefone': fields.String(attribute='cnpj'),
}


class Empresa(db.Model):

    __tablename__ = "tb_empresa"

    id_empresa = db.Column(db.Integer, primary_key=True)
    nome_fantasia = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False, unique=True)

    # voluntario_id = db.Column(db.Integer, db.ForeignKey("tb_voluntario.id_voluntario"))
    # voluntario = db.relationship("Voluntario", uselist=False)

    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return f'Empresa(Nome Fantasia={self.nome_fantasia}, CNPJ={self.cnpj} E-mail={self.email}, Telefone={self.telefone})'