import peewee
from datetime import datetime

db = peewee.SqliteDatabase('database.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Client(BaseModel):
    addrClient = peewee.TextField(unique=True)
    

class IO(BaseModel):
    fromclient = peewee.ForeignKeyField(Client, backref='io')
    messageReciver = peewee.TextField(default=None)
    messageSender = peewee.TextField(default=None)
    timeReciver = peewee.DateTimeField(default=None)
    timeSender = peewee.DateTimeField(default=None)

class Connections(BaseModel):
    fromclient = peewee.ForeignKeyField(Client, backref='connections')
    timeConneticon = peewee.DateTimeField(default=datetime.now())
    timeDisconneticon = peewee.DateTimeField(default=None)
    

try:
    db.create_tables([
        IO,
        Client
    ])
    print("[DATABASE]:\t[OK] ao criar tabela")
except:
    print("[DATABASE]:\t[ERRO] ao criar tabela")
