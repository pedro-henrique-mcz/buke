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