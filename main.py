from src.data.dao.db import get_db
from src.utils import utils
from src.data.dao.person_dao_postgress import PersonDAO
from src.service.person_service import PersonService


db_param = 'json/db.json'
param = utils.load_json(db_param)

db = get_db(param)
person_dao = PersonDAO(db)
person_service = PersonService(person_dao=person_dao)
person_service.set_yesterday()











