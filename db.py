from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    telegram_id = CharField()
    rooms_access = CharField()

    class Meta:
        database = db
