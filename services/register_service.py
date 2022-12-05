import json
from models.student import register, db


def create_logic():
    try:
        # create tables if not exists
        db.create_all()
        db.session.commit()
        print("table created")
        # return "table created"
    except Exception as e:
        print(e)
        return 'table not created'

# def insert_logic():
