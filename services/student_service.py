import json
from models.student import student,db


def create_logic():
    try:
        print('hi')
        #create tables if not exists
        db.create_all()
        db.session.commit()
        return "table created"
    except Exception as e:
        print(e)
        return 'table not created'

# def insert_logic():
    



