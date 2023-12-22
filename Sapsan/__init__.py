from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_restx import Api
from flask import Flask, request, make_response, json, Blueprint
import importlib



app = Flask(__name__)
app.secret_key = 'some secret salt'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/py_Sapsan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://SapsanPlusUser:SapsanPlusUserqwe123@tnnc-sapsan-db:5432/SapsanPlus'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://SapsanPlusUser:SapsanPlusUserqwe123@tnnc-sapsan-db:5432/SapsanPlus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# manager = LoginManager(app)

# from Sapsan import models

from Sapsan import routes
from Sapsan.models import *


blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='''Документация по API для менеджера файлов SapsanPlus''',
    version='1.0',
    description='Микросервис на базе Flask-RESTX',
    doc='/',
)

namespace = routes.namespace
api_extension.add_namespace(namespace)
app.register_blueprint(blueprint)


# @app.route('/stage1')
# def getstage():
#     if request.method == 'GET':
#         print('ffffffffffffffffffffffff')
#         data = Stage.query.all()
#         # data = Stage.filter_by(name='Р').first()

#         # data = Stage
#         print('data ======= ', data)
#         # data = SQlselect(table='spr_stage')
#         # respons = respJson(data)
#         # return respons 


#     with Session(autoflush=False, bind=engine) as db:
#         res = db.query(Stage).all()
#         data = [[str(i.id), i.name] for i in res]
#         print('data = ', data)        