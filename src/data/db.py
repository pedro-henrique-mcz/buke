'''DB connection files'''
import json 
import psycopg2

#taking the dbs infos 
class Connection():
    '''DataBase connection class'''
    def __init__(self, **params):
        if not isinstance(params, dict) or not params:
            raise ValueError(f'param must be a dict type.')

        self._param = params
    
    def _start(self):
        '''Starts the connection'''
        self._conn = psycopg2.connect(**self._param)
        self._cur = self._conn.cursor()
        
    def query(self, query):
        '''Executes some query'''
        self._start()
        self._cur.execute(query)
        self._conn.commit()
        records = self._cur.fetchall()
        
        if records:
            return records
        else:
            return None
        
        self._exit()

    def _exit(self):
        '''Ends the database connection'''
        if self._conn:
            self._conn.close()
        
    
