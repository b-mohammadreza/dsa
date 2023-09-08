from .. import dsu
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

def test_make_set(get_array_list) -> None:
    print('test_make_set(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            dsu_1 = dsu.DisjointSetUnion(arr)
            assert len(dsu_1._collection) == 1

            d_set = dsu_1._collection[0]
            assert d_set[0] == 0

        elif file_name == 'arr_02.json':
            dsu_2 = dsu.DisjointSetUnion(arr)
            assert len(dsu_2._collection) == 3

            d_set_1 = dsu_2._collection[0]
            assert d_set_1['a'] == 'a'

            d_set_2 = dsu_2._collection[1]
            assert d_set_2['b'] == 'b'

            d_set_3 = dsu_2._collection[2]
            assert d_set_3['c'] == 'c'

        elif file_name == 'arr_03.json':
            print(f'test_make_set(): arr->{arr}')

            dsu_3 = dsu.DisjointSetUnion(arr)
            assert len(dsu_3._collection) == 3

            d_set_1 = dsu_3._collection[0]
            print(f'arr_3.json: d_set_1->{d_set_1}')
            assert d_set_1[(0,1)] == (0,1)

            d_set_2 = dsu_3._collection[1]
            print(f'arr_3.json: d_set_2->{d_set_2}')
            assert d_set_2[(0,2)] == (0,2)

            d_set_3 = dsu_3._collection[2]
            print(f'arr_3.json: d_set_3->{d_set_3}')
            assert d_set_3[(1,3)] == (1,3)

    print('test_make_set(): finished...')

def test_find(get_array_list) -> None:
    print('test_find(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            pass

        elif file_name == 'arr_2.json':
            pass

        elif file_name == 'arr_3.json':
            pass

    print('test_find(): finished...')

def test_union(get_array_list) -> None:
    print('test_union(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            pass

        elif file_name == 'arr_2.json':
            pass

        elif file_name == 'arr_3.json':
            pass

    print('test_union(): finished...')
