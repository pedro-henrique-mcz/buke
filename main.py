from src.data.db import Connection
from src.utils import utils
import json

db_param = 'json/db.json'

param = utils.load_json(db_param)


my_connection = Connection(**param)
datas = my_connection.query('SELECT * FROM person')

for data in datas:
    print(data)


