'''PersonDTOParams class' file'''
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class PersonDTOParams:
    '''This function help us to 
    hold and organize the params of the 
    PersonDTO class'''

    person_id : int
    first_name : str
    last_name : str = ""
    nick_name : str = ""
    interaction_frequency : int = 14
    next_interaction : date
    general_notes : str = ""
    category_id : int

    