'''Person's DAO file'''

from src.data.database.db import Connection, get_db 


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


    
        