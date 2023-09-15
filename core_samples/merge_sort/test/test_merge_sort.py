from .. import merge_sort
import pytest
import json
import os

def get_array(struct) -> list:
    arr: list = []
    try:
        arr = struct['arr']
    except ValueError as e:
        print(f'get_array(): "arr" attribute missed: {e}')

    transformed_arr = []
    for item in arr:
        print(f'get_array(): type(item)->{type(item)}')

        if type(item) is list:
            item = tuple(item)
        transformed_arr.append(item)

    return transformed_arr

@pytest.fixture
def get_file_list() -> list[str]:
    return os.listdir('test/arrays')

@pytest.fixture
def get_array_list(get_file_list) -> list[(list, str)]:
    arr_file_list = []

    if len(get_file_list) < 1:
        raise ValueError('get_array_list(): no test-case files found...')

    for json_file in get_file_list: 
        with open(f'test/arrays/{json_file}', 'r') as fstr:
            arr = json.load(fstr, object_hook=get_array)
        arr_file_list.append((arr, json_file))
    
    return arr_file_list

def test_merge_sort(get_array_list) -> None:
    print('test_merge_sort(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            pass

        elif file_name == 'arr_02.json':
            pass

        elif file_name == 'arr_03.json':
            pass

    print('test_merge_sort(): finished...')