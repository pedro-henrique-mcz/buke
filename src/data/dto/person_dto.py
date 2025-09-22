'''PersonDTOParams class' file'''
from dataclasses import dataclass, field
from typing import Optional
import datetime

default_days = 14

@dataclass(frozen=True)
class PersonDTO:
    '''This function help us to 
    hold and organize the params of the 
    PersonDTO class'''

    person_id : Optional[int] = None
    first_name : str = ""
    last_name : str = ""
    nick_name : str = ""
    interaction_frequency : int = default_days
    next_interaction : datetime.date = field(
        default_factory = lambda: datetime.date.today() + datetime.timedelta(days=default_days)
    )
    general_notes : str = ""
    category_id : int = 1

    
