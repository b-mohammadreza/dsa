from .. import bit_man
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

def test_bitwise_and(get_array_list) -> None:
    print('test_bitwise_and(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            assert bit_man.BitManipulation.bitwise_and(arr[0], arr[1]) == 0x20E54

    print('test_bitwise_and(): finished...')

def test_bitwise_or(get_array_list) -> None:
    print('test_bitwise_or(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            assert bit_man.BitManipulation.bitwise_or(arr[0], arr[1]) == 0x1ACFFE

    print('test_bitwise_or(): finished...')

def test_bitwise_xor(get_array_list) -> None:
    print('test_bitwise_xor(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            assert bit_man.BitManipulation.bitwise_xor(arr[0], arr[1]) == 0x18C1AA

    print('test_bitwise_xor(): finished...')

def test_bitwise_not(get_array_list) -> None:
    print('test_bitwise_not(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_02.json':
            assert bit_man.BitManipulation.bitwise_not(arr[0]).to_bytes(length=8, signed=True) == int(0xFFFFFFFFFFF0EF3A).to_bytes(length=8)

    print('test_bitwise_not(): finished...')

def test_bitwise_shift_left(get_array_list) -> None:
    print('test_bitwise_shift_left(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_03.json':
            assert bit_man.BitManipulation.bitwise_shift_left(arr[0], arr[1]) == 0x17534C0

    print('test_bitwise_shift_left(): finished...')

def test_bitwise_shift_right(get_array_list) -> None:
    print('test_bitwise_shift_right(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_03.json':
            assert bit_man.BitManipulation.bitwise_shift_right(arr[0], arr[1]) == 0x5D4D

    print('test_bitwise_shift_right(): finished...')
