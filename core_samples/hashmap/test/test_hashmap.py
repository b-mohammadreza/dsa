from .. import hashmap
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

def test_add_item(get_array_list) -> None:
    print('test_add_item(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            hash_map = hashmap.Hashmap()

            for entry in arr:
                hash_map.add_item(entry[0], entry[1])

            assert hash_map[1] == "value_1"
            assert hash_map[12] == "value_2"
            assert hash_map["3"] == "value_3"
            assert hash_map['25'] == "value_4"
            assert hash_map[10] == "value_5"

        elif file_name == 'arr_02.json':
            hash_map = hashmap.Hashmap()

            for entry in arr:
                hash_map.add_item(entry[0], entry[1])

            assert hash_map[1100] == "value_1"
            assert hash_map['abcd'] == "value_2"
            assert hash_map[900245] == "value_3"

    print('test_add_item(): finished...')

def test_remove_item(get_array_list) -> None:
    print('test_remove_item(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            hash_map = hashmap.Hashmap()

            for entry in arr:
                hash_map.add_item(entry[0], entry[1])

            assert hash_map[1] == "value_1"
            assert hash_map[12] == "value_2"
            assert hash_map["3"] == "value_3"
            assert hash_map['25'] == "value_4"
            assert hash_map[10] == "value_5"

            hash_val = hash('25')
            print(f'hash("25")->{hash_val}')
            assert hash_map.is_valid_hash(hash=hash_val) == True
            
            hash_val = hash(12)
            print(f'hash(12)->{hash_val}')
            assert hash_map.is_valid_hash(hash=hash_val) == True

            hash_map.remove_item('25')
            assert hash_map.length() == 4
            hash_map.remove_item(12)
            assert hash_map.length() == 3

            with pytest.raises(KeyError) as excep_info:
                hash_map.remove_item('20')

            hash_val = hash('20')
            excp_str = str(excep_info.value)
            print(excp_str)

            if hash_map.is_valid_hash(hash=hash_val):
                assert "key->" in excp_str
            else:
                assert "key_hash->" in excp_str

            with pytest.raises(KeyError) as excep_info:
                hash_map.remove_item('25')

            hash_val = hash('25')
            excp_str = str(excep_info.value)
            print(excp_str)

            if hash_map.is_valid_hash(hash=hash_val):
                assert "key->" in excp_str
            else:
                assert "key_hash->" in excp_str

        elif file_name == 'arr_02.json':
            hash_map = hashmap.Hashmap()

            for entry in arr:
                hash_map.add_item(entry[0], entry[1])

            assert hash_map[1100] == "value_1"
            assert hash_map['abcd'] == "value_2"
            assert hash_map[900245] == "value_3"

            hash_val = hash('abcd')
            print(f'hash("abcd")->{hash_val}')
            assert hash_map.is_valid_hash(hash=hash_val) == True
            
            hash_val = hash(900245)
            print(f'hash(900245)->{hash_val}')
            assert hash_map.is_valid_hash(hash=hash_val) == True

            hash_map.remove_item('abcd')
            assert hash_map.length() == 2
            hash_map.remove_item(900245)
            assert hash_map.length() == 1

            with pytest.raises(KeyError) as excep_info:
                hash_map.remove_item(900245)

            hash_val = hash(900245)
            excp_str = str(excep_info.value)
            print(excp_str)

            if hash_map.is_valid_hash(hash=hash_val):
                assert "key->" in excp_str
            else:
                assert "key_hash->" in excp_str

            with pytest.raises(KeyError) as excep_info:
                hash_map.remove_item('aaa')

            hash_val = hash('aaa')
            excp_str = str(excep_info.value)
            print(excp_str)

            if hash_map.is_valid_hash(hash=hash_val):
                assert "key->" in excp_str
            else:
                assert "key_hash->" in excp_str


    print('test_remove_item(): finished...')
