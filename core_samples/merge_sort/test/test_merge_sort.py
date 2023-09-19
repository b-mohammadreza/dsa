from .. import merge_sort
import pytest
import json
import os

from typing import Self

class TestClass:
    """ A test class to test '<' (less than) operator overloading """

    def __init__(self, name, value) -> None:
        self._name = name
        self._value = value

    def __lt__(self, other: Self):
        return self._value < other._value

    def __le__(self, other: Self):
        return self._value <= other._value

def get_array(struct) -> list:
    arr: list = []
    try:
        data_type:str = struct['data_type']
    except ValueError as e:
        print(f'get_array(): "data_type" attribute missed: {e}')

    try:
        arr = struct['arr']
    except ValueError as e:
        print(f'get_array(): "arr" attribute missed: {e}')

    if data_type != "TestClass":
        return arr

    if data_type == "TestClass":
        transformed_arr = []

        for item in arr:
            print(f'get_array(): item->{item}')

            if type(item) is not list:
                print('get_array(): Costructing "TestClass" objects. "item" type must be "list".')
                raise ValueError

            elif len(item) < 2:
                print('get_array(): Costructing "TestClass" objects. "item" length must be greater than 1.')
                raise ValueError

            elif type(item[0]) is not str:
                print('get_array(): Costructing "TestClass" objects. "item[0]" type must be "str".')
                raise ValueError

            elif type(item[1]) is not int:
                print('get_array(): Costructing "TestClass" objects. "item[1]" type must be "int".')
                raise ValueError

            else:
                test_obj: TestClass = TestClass(item[0], item[1])
                transformed_arr.append(test_obj)

        return transformed_arr

    return []

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
            assert merge_sort.msort(arr) == [1,5,7,7,10,12]

        elif file_name == 'arr_02.json':
            assert merge_sort.msort(arr) == [1,23,30,89,100]

        elif file_name == 'arr_03.json':
            assert merge_sort.msort(arr) == [1,3]

        elif file_name == 'arr_04.json':
            sorted_arr: list[TestClass] = merge_sort.msort(arr)
            assert sorted_arr[0]._name == "2nd_instance"
            assert sorted_arr[0]._value == 20

            assert sorted_arr[1]._name == "1st_instance"
            assert sorted_arr[1]._value == 89

            assert sorted_arr[2]._name == "3rd_instance"
            assert sorted_arr[2]._value == 1908


    print('test_merge_sort(): finished...')