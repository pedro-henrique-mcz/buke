'''Person's DAO file'''
from src.data.database.db import Connection 
from src.data.dto.person_dto import PersonDTO
from psycopg2.extras import RealDictCursor

class PersonDAO():
    '''Person DAO class'''
    def __init__(self, conn : Connection) -> None:
        '''Person DAO constructor class'''
        try: 
            if not isinstance(conn, Connection) or not conn:
                raise ValueError
        except ValueError:
            print('"conn" must be a non empty Connection type.')
            pass

        self._conn = conn

    def get_by_id(self, id:int ) -> PersonDTO|None:
        '''Read from Crud'''
        try: 
            if not isinstance(id, int) or not id:
                raise ValueError
        except ValueError:
            print('"id" must be a non empty int type.')
            pass

        with self._conn as conn:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(f"SELECT * FROM person WHERE person_id = {id}")
            row = cur.fetchone()
            

        if row:
            return PersonDTO(**row)
        else:
            return None
   
    def get_persons(self) ->list[PersonDTO]|None:
        '''Search for all item from the Person table in the BD'''
        with self._conn as conn:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute('SELECT * FROM person;')
            rows = cur.fetchall()
        
        if rows:
            return rows
        else:
            return None
    
    def create(self, person) -> True:
        '''Create a Person into de the BD'''
        with self._conn as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO person (
                first_name, 
                last_name, 
                nick_name,
                interaction_frequency,
                next_interaction,
                general_notes,
                category_id
            ) 
            VALUES (
                %(first_name)s, 
                %(last_name)s, 
                %(nick_name)s,
                %(interaction_frequency)s,
                %(next_interaction)s,
                %(general_notes)s,
                %(category_id)s
            )
        """,
        person)

        return True
    
    def update(self, person: dict) ->True:
        '''Update some info from person table'''
        with self._conn as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE person
                SET first_name = 
                    first_name = %(first_name)s,
                    last_name = %(last_name)s,
                    nick_name =%(nick_name)s,
                    interaction_frequency = %(interaction_frequency)s,
                    next_interaction = %(next_interaction)s,
                    general_notes = %(general_notes)s,
                    category_id =%(category_id)s
                WHERE person_id =  %(person_id)s
            """, person)
            return True

    def delete(self, person_id:int):
        '''Delete person in table'''
        with self._conn as conn:
            cur = conn.cursor()
            cur.execute(f'DELETE FROM person WHERE person_id = {person_id};')
            return True

        