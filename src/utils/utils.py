'''Supporte Module'''
import json


def load_json(path):
    '''Support function to open files'''
    try:
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f'Error:{e}.')
    except  json.JSONDecodeError as e:
        print(f'Error:{e}.')
    else:
        return data
    
def data_validation(data_type, correct_type, name):
    '''This function allow us to check datats types
    in the class construction'''
    
    # pro predict wrong params
    # data_type = type that we are receving
    # correct_type = type that we excpect
    # name = data's name
    try: 
        if not isinstance(data_type, correct_type) or not data_type:
            raise ValueError
    except ValueError:
        err_message = f'The "{name}", must be a {correct_type}.'
        err_message += '\n{data_type} given.'
        print(err_message) 

    return True