from peewee import *
from hafez import config

conn = MySQLDatabase(
    config.db_name,
    user = config.db_user,
    password = config.db_password,
    host = config.db_host,
)

class BaseModel(Model):
    class Meta:
        database = conn
