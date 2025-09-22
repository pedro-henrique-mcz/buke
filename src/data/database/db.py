'''DB connection wrapper'''

import psycopg2

class Connection():
    '''DB sesion class wrapper'''
    def __init__(self, param:dict) -> None:

        try: 
            if not isinstance(param, dict) or not param:
                raise ValueError
        except ValueError:
            print(f'Alert! Param arg must be a non empty dict type.')
            pass
        
        self._param = param

    def __enter__(self):
        '''This method allows us to use the open
        built in function, for more datils check the
        open function in Python documentation'''
        try:
            self._conn = psycopg2.connect(
                host = self._param['host'],
                port = self._param['port'],
                dbname = self._param['dbname'],
                user = self._param['user'],
                password = self._param['password']
            )
            return self._conn
        except psycopg2.OperationalError:
            print('Alert! The database is inaccessible.')
            pass
    

    def __exit__(self,  exc_type, exc_val, exc_tb):
        '''This method allows us to use the open
        built in function, for more datils check the
        open function in Python documentation'''
        self._conn.commit()
        self._conn.close()

def get_db(param):
    return Connection(param)

    

