from .. import stack
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
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.is_empty() == True

        elif file_name == 'arr_02.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.is_empty() == False

    print('is_empty(): finished...')

def test_peek(get_array_list) -> None:
    print('test_peek(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.peek() == None

        elif file_name == 'arr_02.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.peek() == 4

    print('test_peek(): finished...')

def test_push(get_array_list) -> None:
    print('test_push(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.peek() == None

        elif file_name == 'arr_02.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)
                assert s.peek() == item

            assert s.peek() == 4

    print('test_push(): finished...')

def test_pop(get_array_list) -> None:
    print('test_pop(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)

            assert s.pop() == None

        elif file_name == 'arr_02.json':
            s: stack.Stack = stack.Stack()

            for item in arr:
                s.push(item)
                assert s.peek() == item

            for _ in range(len(arr)):
                peek_item = s.peek()
                pop_item = s.pop()
                assert peek_item == pop_item

            assert s.pop() == None

    print('test_pop(): finished...')
