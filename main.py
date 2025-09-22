from src.data.database.db import get_db
from src.utils import utils
from src.data.database.person_dao_postgress import PersonDAO
from src.data.dto.person_dto_schema import PersonDTOSchema
from src.data.dto.person_dto import PersonDTO
from pprint import pprint

db_param = 'json/db.json'
param = utils.load_json(db_param)

db = get_db(param)
person_dao = PersonDAO(db)

antonio = person_dao.get_by_id(2)
person_schema = PersonDTOSchema()
result = person_schema.dump(antonio)
result['nick_name'] = 'Tonho'
person_dao.update(result)
print(result['person_id'])
person_dao.delete(person_id=result['person_id'])









