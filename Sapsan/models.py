# from flask_login import UserMixin
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy import ForeignKey

from Sapsan import db

Base = declarative_base()


class DefaultClass111():
    __table_args__ = {'schema': 'dbo'}
    id = Column(UNIQUEIDENTIFIER(), primary_key=True, index=True)

    def toObj(self):
        obj = {}
        cols = self.__table__.columns.keys()
        # print('cols = ', cols)
        for key in cols:
            obj[key] = str(self.__getattribute__(key))
        return obj


class Contract(db.Model, DefaultClass111):
    shifr = Column(String)
    subject = Column(String)

    
class Spr_stage(db.Model, DefaultClass111):
    name = Column(String)
    description = Column(String)
    order_num = Column(String)

    pr = db.relationship('Complect', backref='prR')


    def __repr__(self):
        return f"{self.toObj()}"



class Complect(db.Model, DefaultClass111):
    shifr = Column(String())
    id_contract = Column(UNIQUEIDENTIFIER())
    tom_name = Column(String())
    status = Column(String())
    id_stage = Column(Integer(), ForeignKey(Spr_stage.id))



    # prR = db.relationship('Spr_stage', backref='pr')

    # id_stage = Column(UNIQUEIDENTIFIER())
    # id_stage = Column(Integer, ForeignKey('Spr_stage.id'))
    # pr = db.relationship("Spr_stage")
    # name = db.relationship("Spr_stage", backref="Complect")

    # id_stage = Column(Integer(), ForeignKey('Spr_stage.id'))
    # id_stage = Column(db.ForeignKey(Spr_stage.id))
    # root = db.relationship(Spr_stage, backref='paths')

    # id_stage = db.Column(db.Integer, db.ForeignKey(Spr_stage.id))




    

    def __repr__(self):
        return f"{self.toObj()}"

class Contract_etap(db.Model, DefaultClass111):
    name = Column(String)


class Spr_mark(db.Model, DefaultClass111):
    name = Column(String)
    descriptio = Column(String)

# def rejson(cls):
#     obj = {}
#     for key in cls.__table__.columns.keys():
#         obj[key] = str(cls.__getattribute__(key))
#     # print('obj = ', obj)
#     return obj



# class Spr_stage(db.Model):
#     # __tablename__ = "spr_stage"
#     __table_args__ = {'schema': 'dbo'}
#     id = Column(UNIQUEIDENTIFIER, primary_key=True, index=True)
#     name = Column(String)
#     description = Column(String)
    
#     def toObj(self):
#         return rejson(self)
    
#     def __repr__(self):
#         return f"{self.toObj()}"