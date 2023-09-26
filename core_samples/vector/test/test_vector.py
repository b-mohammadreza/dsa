from .. import vector
import pytest
import json
import os

from typing import Self,Any

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

def test_is_empty(get_array_list) -> None:
    print('is_empty(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.is_empty() == True

        elif file_name == 'arr_02.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.is_empty() == False

    print('is_empty(): finished...')

def test_at(get_array_list) -> None:
    print('test_at(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.at(0) == None

        elif file_name == 'arr_02.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.at(2) == 3
            assert v.at(1) == 2

    print('test_at(): finished...')

def test_insert(get_array_list) -> None:
    print('test_insert(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.back() == None

        elif file_name == 'arr_02.json':
            v: vector.Vector = vector.Vector()

            for index, item in enumerate(arr):
                v.insert(index, item)
                assert v.size() == index+1
                assert v.back() == item

            assert v.at(3) == 4
            assert v.at(0) == 1

    print('test_insert(): finished...')

def test_erase(get_array_list) -> None:
    print('test_erase(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.pop_back() == None

        elif file_name == 'arr_02.json':
            v: vector.Vector = vector.Vector()

            for item in arr:
                v.push_back(item)

            assert v.front() == 1
            assert v.back() == 4

            assert 3 == v.at(2)
            assert 3 == v.erase(2)

            assert 2 == v.at(1)
            assert 2 == v.erase(1)

            assert 4 == v.at(1)
            assert 4 == v.erase(1)

            assert 1 == v.at(0)
            assert 1 == v.erase(0)

            assert v.pop_back() == None

    print('test_erase(): finished...')
