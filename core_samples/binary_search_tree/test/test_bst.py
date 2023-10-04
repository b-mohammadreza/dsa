from .. import bst
import pytest
import json
import os

from typing import Any

@pytest.fixture
def get_file_list() -> list[str]:
    return os.listdir('test/arrays')

@pytest.fixture
def get_array_list(get_file_list) -> list[(list[int], str)]:
    arr_file_list = []

    if len(get_file_list) < 1:
        raise ValueError('get_array_list(): no test-case files found...')

    for json_file in get_file_list: 
        with open(f'test/arrays/{json_file}', 'r') as fstr:
            file_data = json.load(fstr)

        try:
            arr = get_array(file_data['data_type'], file_data['arr'])
            arr_file_list.append((arr, json_file))

        except ValueError as e:
            print(f'fixture: get_array_list(): One of the attributes("data_type" or "arr")\
                   is missing in the {json_file} file. Description: {e}')
    
    return arr_file_list

def get_array(data_type: str, arr: list[Any]) -> list[Any]:
    # ignoring data_type for now.
    return arr

def test_1(get_array_list) -> None:
    print('test_1(): started...')
    print('test_1(): finished...')
