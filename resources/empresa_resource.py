from flask import jsonify
from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db
from model.empresa_model import Empresa, empresa_fields
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('nome_fantasia', required=True)
parser.add_argument('cnpj', required=True)
parser.add_argument('email', required=True)
parser.add_argument('telefone', required=True)

class EmpresaResource(Resource):

    @marshal_with(empresa_fields)
    def get(self):
        current_app.logger.info("Get - Empresas")
        empresa = Empresa.query\
            .all()
        return empresa, 200
    
    def post(self):
        current_app.logger.info("Post - Parceiros")
        try:
            # JSON
            args = parser.parse_args()
            nome_fantasia = args['nome_fantasia']
            cnpj = args['cnpj']
            email = args['email']
            telefone = args['telefone']

            empresa = Empresa(nome_fantasia, cnpj, email, telefone)
            
            db.session.add(empresa)
            db.session.commit()
            
            return 200

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

class EmpresaById(Resource):    
    def put(self, id_empresa):
        current_app.logger.info("Put - Empresa")
        try:
         # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Empresa: %s:" % args)
            #json

            nome_fantasia = args['nome_fantasia']
            cnpj = args['cnpj']
            email = args['email']
            telefone = args['telefone']
            
            empresa =Empresa.query \
                .filter_by(id_empresa=id_empresa) \
                .first()
            
            empresa.nome_fantasia = nome_fantasia
            empresa.cnpj = cnpj
            empresa.email = email
            empresa.telefone = telefone
            
            db.session.commit()
            
        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, id_empresa):
        try:
            empresa = Empresa.query.filter_by(id_empresa=id_empresa).first()
            
            if empresa:

                db.session.delete(empresa)
                db.session.commit()
                
                return 204
            else:
                return 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500