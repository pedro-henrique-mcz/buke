'''Person Service Class'''
from src.data.dao.person_dao_postgress import PersonDAO
from random import shuffle
from datetime import date, timedelta

class PersonService():
    '''Person Service class'''
    def __init__(self, person_dao : PersonDAO):
        '''Person Service's constructor class'''
        self._controller = person_dao

    def shuffle(self) -> True:
        '''This function will shuffle the 
        person's date colum in person's table'''
        

        #This fucntion works getting the total of persons
        #in bd in a list and shuffling it, the new positions 
        #of the list will be the new_interactions days for the program.
        rows = self._controller.get_persons()
        shuffle(rows)
        total_person = len(rows)

        for i in range(total_person):
            new_date = date.today() + timedelta(days=i)
            rows[i]['next_interaction'] = new_date
            self._controller.update(rows[i])

        return True
    
    def set_today(self):
        '''The main core of the program, this will 
        organize the persons position.'''

        #setting the yesterday person for the next interaction
        today_person = self._controller.get_person_by_date(date.today())
        return today_person
    
    def set_yesterday(self):
        '''setting the yesterday person for the next interaction'''
        yesterday = date.today() - timedelta(days=1)
        last_person = self._controller.get_person_by_date(yesterday)
         
        if last_person:
            next_day = len(self._controller.get_persons())
            last_person['next_interaction'] += timedelta(days=next_day)
            self._controller.update(last_person)