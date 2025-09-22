from src.data.database.db import get_db
from src.utils import utils

db_param = 'json/db.json'
param = utils.load_json(db_param)

with get_db(param) as db:
    cur = db.cursor()
    cur.execute('SELECT * FROM person;')
    rows = cur.fetchall()
    for row in rows:
        print(row)

