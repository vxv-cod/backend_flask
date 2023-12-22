# blueprints/final_servis/primery_api/__init__.py
import os
import sys
from flask import make_response, json, jsonify, Response, request, url_for
from sqlalchemy import create_engine
from sqlalchemy import inspect
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
# from sqlalchemy.orm import class_mapper, ColumnProperty

# from app import contract

# from rich import print

from functions import *
from Sapsan.state.query_SQL_for_db import *
from Sapsan.models import *
# import Sapsan.models as mod
from Sapsan import db






namespace = Namespace(
    name='ContractApi', 
    description='Примеры API запросов, оперирующих сущностями', 
    path='/',
)


# def def_getBy(class_name, filter_id):
#     if filter_id == None:
#         '''Получение по созданному классу в models.py всех данных из базы '''
#         return  db.session.query(class_name).all()
#     else:
#         '''Получение по созданному классу в models.py данных из базы по id'''
#         return  db.session.query(class_name).filter(class_name.id == filter_id).all()


# def respo(class_name, filter_id=None):
#     '''Получение данных из базы по созданному классу в models.py'''
#     data =  [i.toObj() for i in def_getBy(class_name, filter_id)]
#     response = make_response(json.dumps(data, ensure_ascii = False, indent=4, sort_keys=True))
#     response.headers['Content-Type'] = 'application/json; charset=utf-8'
#     return response


def respJson(data):
    response = make_response(json.dumps(data, ensure_ascii = False, indent=4, sort_keys=True))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


def saveJsonFile(name, data):
    with open(f'{name}.json', 'w') as f:
        json.dump(data, f, indent=4)


class defaultClassRout:
    def _id(self):
        args = request.args.to_dict()
        id = args['id'] if args != {} else None
        return id

    def items(self, class_name):
        filter_id = self._id()
        if filter_id == None:
            '''Получение по созданному классу в models.py всех данных из базы '''
            return db.session.query(class_name).all()
        else:
            '''Получение по созданному классу в models.py данных из базы по id'''
            return db.session.query(class_name).filter(class_name.id == filter_id).all()

    def respo(self, class_name):
        '''Собираем список из строк с именами ячеек в каждой строке таблицы'''
        items = self.items(class_name)
        print('ggggggggggggg ', type(items[0]), items[0], type(items))
        # cols = items[0].keys()
        # data = [{cols[i] : str(row[i]) for i in range(len(cols))} for row in items]        
        data =  [i.toObj() for i in items]
        '''Джейсоним ответ'''
        response = make_response(json.dumps(data, ensure_ascii = False, indent=4, sort_keys=True))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response    

# query.outerjoin(Order, Order.user_id == User.id)
    
# http://127.0.0.1:5000/api/contract
# ?id=FC0B0A2A-BADF-4DEB-8971-0075AEBE3388&shifr=1111
@namespace.route('/contracts')
class GetContracts(Resource, defaultClassRout):
    def get(self):
        return self.respo(Contract)


# http://127.0.0.1:5000/api/stage/
@namespace.route('/stages')
class GetStages(Resource, defaultClassRout):
    def get(self):
        return self.respo(Spr_stage)



# http://127.0.0.1:5000/api/complect/
@namespace.route('/complects')
class GetComplect(Resource, defaultClassRout):
    def get(self):
        items = db.session.query(
            Complect.id, 
            Complect.tom_name, 
            Spr_stage.name, 
            Spr_stage.description
        )
        items = items.join(Complect, Complect.id_stage == Spr_stage.id)[:3]
        print('ggggggggggggg ', type(items), type(items[0]), items[0], isinstance(items, list))

        cols = list(items[0]._mapping)
        print(list(items[0]._mapping))
        data = [{cols[i] : str(row[i]) for i in range(len(cols))} for row in items]
        return respJson(data)

        # return self.respo(Complect)


# import sqlalchemy

# http://127.0.0.1:5000/api/complect/
@namespace.route('/complects1')
class GetComplect1(Resource, defaultClassRout):
    def get(self):
    #     items = db.session.query(
    #         Complect, 
    #         Spr_stage.name, 
    #         # Spr_stage.description
    #     )
        # items = items.join(Complect, Complect.id_stage == Spr_stage.id)[:3]
        # print('ggggggggggggg ', type(items), type(items[0]), items[0], isinstance(items, list))
        # print('ggggggggggggg ', dir(sqlalchemy.engine.row.Row))
        # print('items[0]._data =  ', items[0]._data)
        # print('\n')
        # print('list(items[0]._data =  ', list(items[0]._data))
        # print('\n')
        # print('list = items[0]._mapping =  ', list(items[0]._mapping.values()))
        # print('\n')
        # print('items[0]._mapping =  ', items[0]._mapping)
        # print('\n')
        # print(list(items[0]._mapping))

        # data = dict(items[0]._mapping)
        # data = [row._mapping.items() for row in items]

        # print('data = ', data)
        # return respJson(data)
        # print('\n')
        
        
        # items = db.session.query(Complect, Spr_stage).join(Complect, Complect.id_stage == Spr_stage.id)
        # items = db.session.query(Complect)
        # print('items = ', items)
        # items = items.first()
        # print('\n')
        # print(
        #     'Complect_items = ', 
        #     items.first().__table__.columns.keys(), 
        #     items.first().prR.name
        #     )
        print('\n')

        # items =  db.session.query(Complect)[:1]
        # items = Complect.query[:3]
        items = db.session.query(Complect, Complect.name)[:1]

        print('items = ', items)
        
        # print('items = ', items[0].prR.name)

        # print('respoo = ', items)
        # data =  [i.toObj() for i in items]
        # print('data = ', data)





        # print('items = ', db.session.query(Spr_stage).first().__table__.columns.keys())

        # items = Complect.query.join(Spr_stage, (Complect.id == Spr_stage.id))
        # items = Complect.query()
        # print('items Complect.query = ', items)

        # print('\n')
        # items = items.first()
        # print('items = ', items)
        # print('\n')



        # return self.respo(Complect)



# if __name__ == "__main__":
#     app.run(debug=True)        



# classname = __class__.__name__
# print('class ============ ', getattr(mod, __class__.__name__))
# return respo(getattr(mod, __class__.__name__), self._id())
        # return respo(mod.Spr_stage, self._id())
