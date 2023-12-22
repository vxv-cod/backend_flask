"""Модуль отправки данный на MS SQL 2017 server силами Python"""
# from flask import make_response
from datetime import datetime
import pyodbc
import json
# from rich import print

# import psycopg2

# connect_text = '''
#     Driver={SQL Server};
#     Server=tnnc-sapsan-db;
#     Database=SapsanPlus;
#     '''
connect_text = '''
    DRIVER={PostgreSQL UNICODE};
    DATABASE=SapsanPlus;
    UID=SapsanPlusUser;
    PWD=SapsanPlusUserqwe123;
    SERVER=tnnc-sapsan-db;
    PORT=5432;
    '''

def SQlselect(table, columns=None, dictargs={}):
    '''Выполним соединение к нашей базе данных:'''
    connection = pyodbc.connect(connect_text)
    # connection = psycopg2.connect(connect_text)

    '''Создадим курсор, с помощью которого, посредством передачи 
    запросов будем оперировать данными в нашей таблице:'''
    cursor = connection.cursor()
    if columns == None:
        columns = getColName(table)
    columnsstring = ', '.join(columns)
    '''Добавим данные в нашу таблицу с помощью кода на python:'''
    if dictargs == {}:
        text = f''' SELECT {columnsstring} 
                    FROM dbo.{table}
                '''
    else:
        dictargs = list(dictargs.columnss())
        name, value = dictargs[0]
        text = f''' SELECT {columnsstring} 
                    FROM dbo.{table} 
                    where {name} = "{value}"
                '''
    cursor.execute(text)
    '''Возвращаем список всех доступных строк в запросе'''
    rows = cursor.fetchall()

    '''Каждой строке по элементно присваиваем ключи к значениям'''
    data = []
    for row in rows:
        data.append({columns[i] : str(row[i]) for i in range(len(columns))})

    cursor.close()
    connection.close()

    # print(f'data = {data}')

    return data



def getColName(table):
    with pyodbc.connect(connect_text) as connection:
        cursor = connection.cursor()
        # text = f''' SELECT column_name, column_default, data_type
        text = f''' SELECT column_name
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE table_name = '{table}' AND table_schema = 'dbo'
                '''
        cursor.execute(text)
        data = [row[0] for row in cursor.fetchall()]
        print('getColName = ', data)
        cursor.close()
        return data





def SQlquery(text, columns=None):
    # print(pyodbc.drivers())
    with pyodbc.connect(connect_text) as connection:
        cursor = connection.cursor()
        cursor.execute(text)
        fetch = cursor.fetchall()
        # data = [{columns[i] : list(row)[i] for i in range(len(columns))} for row in cursor.fetchall()]
        data = [list(row) for row in fetch]
        # print('data = ', data)

    return data

def SQl_select_all(table, columns=[]):
    # print(pyodbc.drivers())
    def dateformat(typed, date):
        # print('type = ', typed, type(typed))
        if "timestamp" in typed and  date != None:
        # if isinstance(date, None):
            print('date = ', date, type(date), typed)

            t = datetime.fromisoformat(str(date)).strftime('%d.%m.%Y')
            print('ttttt ==== ', t)
            return str(t)
        return str(date)
    
    data = []
    with pyodbc.connect(connect_text, readonly=True) as connection:
        with connection.cursor() as cursor:
            if columns == []:
                cursor.execute(f''' SELECT column_name, data_type
                                    FROM INFORMATION_SCHEMA.COLUMNS 
                                    WHERE table_name = '{table}' AND table_schema = 'dbo'
                                ''')
                columns_fetchall = cursor.fetchall()
                data_type = {row[0] : row[1] for row in columns_fetchall}
                print('data_type = ', data_type)
                columns = [row[0] for row in columns_fetchall]
            columnString = ', '.join(columns)
            cursor.execute(f'SELECT {columnString} FROM dbo.{table}')
            # data = [{columns[i] : str(row[i]) for i in range(len(columns))} for row in cursor.fetchall()]
            data = [{columns[i] : dateformat(data_type[columns[i]], row[i]) for i in range(len(columns))} for row in cursor.fetchall()]
            data.append({'data_type': data_type})
    return data
