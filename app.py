from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from helpers.database import db, migrate

from model.empresa_model import Empresa
from resources.empresa_resource import EmpresaResource, EmpresaById

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/flaskdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)



empresa = Empresa("DLC", "5464897987", "dlc@mail.com", "89798787987")
print(empresa)

api.add_resource(EmpresaResource, '/empresas')
api.add_resource(EmpresaById, '/empresas/<id_empresa>')

if __name__ == '__main__':
    app.run(debug=False)