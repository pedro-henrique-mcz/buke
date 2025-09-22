'''Person's DTO file'''
from dataclasses import dataclass
from src.data.dto.person_dto_params import PersonDTOParams

@dataclass
class PersonDTO:
    '''Person DTO class'''
    def __init__(self, data : PersonDTOParams) -> None:
        '''PersonDTO class' constructor'''
    pass   
       

