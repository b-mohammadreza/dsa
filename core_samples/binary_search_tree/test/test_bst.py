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

def test_add_node(get_array_list) -> None:
    print('test_add_node(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            bstree = bst.BST(arr, False)

            assert bstree._root != None

            assert bstree._root._value == 1
            assert bstree._root._lheight == 0
            assert bstree._root._rheight == 3

            assert bstree._root._left == None
            assert bstree._root._parent == None

            assert bstree._root._right._value == 12
            assert bstree._root._right._lheight == 2
            assert bstree._root._right._rheight  == 1

            assert bstree._root._right._parent._value  == 1

            assert bstree._root._right._left._value == 3
            assert bstree._root._right._left._lheight == 0
            assert bstree._root._right._left._rheight == 1

            assert bstree._root._right._left._parent._value == 12

            assert bstree._root._right._left._right._value == 10
            assert bstree._root._right._left._right._lheight == 0
            assert bstree._root._right._left._right._rheight == 0

            assert bstree._root._right._left._right._parent._value == 3

            assert bstree._root._right._right._value == 25
            assert bstree._root._right._right._lheight == 0
            assert bstree._root._right._right._rheight == 0

            assert bstree._root._right._right._parent._value == 12

        elif file_name == 'arr_02.json':
            bstree = bst.BST(arr, False)

            assert bstree._root != None

            assert bstree._root._value == 3
            assert bstree._root._lheight == 1
            assert bstree._root._rheight == 2

            assert bstree._root._parent == None

            assert bstree._root._left._value == 1
            assert bstree._root._left._lheight == 0
            assert bstree._root._left._rheight  == 0

            assert bstree._root._left._parent._value  == 3

            assert bstree._root._right._value == 5
            assert bstree._root._right._lheight == 1
            assert bstree._root._right._rheight  == 0

            assert bstree._root._right._parent._value  == 3

            assert bstree._root._right._left._value == 4
            assert bstree._root._right._left._lheight == 0
            assert bstree._root._right._left._rheight == 0

            assert bstree._root._right._left._parent._value == 5

        elif file_name == 'arr_04.json':
            bstree = bst.BST(arr, True)

            assert bstree._root._value == 6
            assert bstree._root._lheight == 2
            assert bstree._root._rheight == 1

            assert bstree._root._left._value == 3
            assert bstree._root._left._lheight == 0
            assert bstree._root._left._rheight == 1

            assert bstree._root._left._right._value == 5
            assert bstree._root._left._right._lheight == 0
            assert bstree._root._left._right._rheight == 0

            assert bstree._root._right._value == 7
            assert bstree._root._right._lheight == 0
            assert bstree._root._right._rheight == 0

        elif file_name == 'arr_05.json':
            bstree = bst.BST(arr, True)

            assert bstree._root._value == 5
            assert bstree._root._lheight == 2
            assert bstree._root._rheight == 1

            assert bstree._root._left._value == 3
            assert bstree._root._left._lheight == 0
            assert bstree._root._left._rheight == 1

            assert bstree._root._left._right._value == 4
            assert bstree._root._left._right._lheight == 0
            assert bstree._root._left._right._rheight == 0

            assert bstree._root._right._value == 6
            assert bstree._root._right._lheight == 0
            assert bstree._root._right._rheight == 0

        elif file_name == 'arr_06.json':
            bstree = bst.BST(arr, True)

            assert bstree._root._value == 9
            assert bstree._root._lheight == 2
            assert bstree._root._rheight == 1

            assert bstree._root._left._value == 8
            assert bstree._root._left._lheight == 1
            assert bstree._root._left._rheight == 0

            assert bstree._root._left._left._value == 5
            assert bstree._root._left._left._lheight == 0
            assert bstree._root._left._left._rheight == 0

            assert bstree._root._right._value == 10
            assert bstree._root._right._lheight == 0
            assert bstree._root._right._rheight == 0

        elif file_name == 'arr_07.json':
            bstree = bst.BST(arr, True)

            assert bstree._root._value == 7
            assert bstree._root._lheight == 1
            assert bstree._root._rheight == 2

            assert bstree._root._left._value == 6
            assert bstree._root._left._lheight == 0
            assert bstree._root._left._rheight == 0

            assert bstree._root._right._value == 10
            assert bstree._root._right._lheight == 1
            assert bstree._root._right._rheight == 0

            assert bstree._root._right._left._value == 8
            assert bstree._root._right._left._lheight == 0
            assert bstree._root._right._left._rheight == 0
            

    print('test_add_node(): finished...')

def test_remove_node(get_array_list) -> None:
    print('test_remove_node(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_01.json':
            bstree_0 = bst.BST(arr, False)

            bstree_0.remove_node(bstree_0._root, 1, False)
            assert bstree_0._root._value == 12
            assert bstree_0._root._left._value == 3
            assert bstree_0._root._right._value == 25

            bstree_0.remove_node(bstree_0._root, 12, False)
            assert bstree_0._root._value == 25
            assert bstree_0._root._left._value == 3
            assert bstree_0._root._left._left == None
            assert bstree_0._root._left._right._value == 10
            assert bstree_0._root._right == None


            bstree_1 = bst.BST(arr, True)

            bstree_1.remove_node(bstree_1._root, 1, True)
            assert bstree_1._root._value == 12
            assert bstree_1._root._left._value == 3
            assert bstree_1._root._left._right._value == 10
            assert bstree_1._root._right._value == 25

        elif file_name == 'arr_02.json':
            bstree_0 = bst.BST(arr, False)

            bstree_0.remove_node(bstree_0._root, 1, False)
            assert bstree_0._root._value == 3
            assert bstree_0._root._lheight == 0
            assert bstree_0._root._rheight == 2

            assert bstree_0._root._left == None

            assert bstree_0._root._right._value == 5
            assert bstree_0._root._right._lheight == 1
            assert bstree_0._root._right._rheight == 0

            assert bstree_0._root._right._left._value == 4
            assert bstree_0._root._right._left._lheight == 0
            assert bstree_0._root._right._left._rheight == 0

            bstree_1 = bst.BST(arr, True)

            bstree_1.remove_node(bstree_1._root, 1, True)
            assert bstree_1._root._value == 4
            assert bstree_1._root._lheight == 1
            assert bstree_1._root._rheight == 1

            assert bstree_1._root._left._value == 3

            assert bstree_1._root._right._value == 5
            assert bstree_1._root._right._lheight == 0
            assert bstree_1._root._right._rheight == 0

            bstree_0.remove_node(bstree_0._root, 5, False)
            assert bstree_0._root._value == 3
            assert bstree_0._root._lheight == 0
            assert bstree_0._root._rheight == 1

            assert bstree_0._root._left == None

            assert bstree_0._root._right._value == 4
            assert bstree_0._root._right._lheight == 0
            assert bstree_0._root._right._rheight == 0

            assert bstree_0._root._right._left == None
            assert bstree_0._root._right._right == None

        elif file_name == 'arr_03.json':
            bstree_0 = bst.BST(arr, False)

            assert bstree_0._root._lheight == 2
            assert bstree_0._root._rheight == 6

            assert bstree_0._root._left._lheight == 1
            assert bstree_0._root._left._rheight == 1

            assert bstree_0._root._left._right._lheight == 0
            assert bstree_0._root._left._right._rheight == 0

            assert bstree_0._root._left._left._lheight == 0
            assert bstree_0._root._left._left._rheight == 0

            assert bstree_0._root._right._lheight == 2
            assert bstree_0._root._right._rheight == 5

            assert bstree_0._root._right._left._lheight == 1
            assert bstree_0._root._right._left._rheight == 1

            assert bstree_0._root._right._left._left._lheight == 0
            assert bstree_0._root._right._left._left._rheight == 0
            assert bstree_0._root._right._left._right._lheight == 0
            assert bstree_0._root._right._left._right._rheight == 0

            assert bstree_0._root._right._right._lheight == 4
            assert bstree_0._root._right._right._rheight == 2

            assert bstree_0._root._right._right._left._lheight == 3
            assert bstree_0._root._right._right._left._rheight == 0

            assert bstree_0._root._right._right._left._left._lheight == 0
            assert bstree_0._root._right._right._left._left._rheight == 2

            assert bstree_0._root._right._right._left._left._right._lheight == 1
            assert bstree_0._root._right._right._left._left._right._rheight == 1

            assert bstree_0._root._right._right._left._left._right._right._lheight == 0
            assert bstree_0._root._right._right._left._left._right._right._rheight == 0
            assert bstree_0._root._right._right._left._left._right._left._lheight == 0
            assert bstree_0._root._right._right._left._left._right._left._rheight == 0

            assert bstree_0._root._right._right._right._lheight == 0
            assert bstree_0._root._right._right._right._rheight == 1

            assert bstree_0._root._right._right._right._right._lheight == 0
            assert bstree_0._root._right._right._right._right._rheight == 0

            bstree_0.remove_node(bstree_0._root, 30, False)
            assert bstree_0._root._value == 12
            assert bstree_0._root._lheight == 2
            assert bstree_0._root._rheight == 5

            assert bstree_0._root._left._value == 10
            assert bstree_0._root._left._lheight == 1
            assert bstree_0._root._left._rheight == 1

            assert bstree_0._root._left._right._value == 11
            assert bstree_0._root._left._right._lheight == 0
            assert bstree_0._root._left._right._rheight == 0

            assert bstree_0._root._left._right._left == None
            assert bstree_0._root._left._right._right == None

            assert bstree_0._root._left._left._value == 8
            assert bstree_0._root._left._left._lheight == 0
            assert bstree_0._root._left._left._rheight == 0

            assert bstree_0._root._left._left._left == None
            assert bstree_0._root._left._left._right == None

            assert bstree_0._root._right._value == 33
            assert bstree_0._root._right._lheight == 2
            assert bstree_0._root._right._rheight == 4

            assert bstree_0._root._right._left._value == 15
            assert bstree_0._root._right._left._lheight == 1
            assert bstree_0._root._right._left._rheight == 1

            assert bstree_0._root._right._left._left._value == 13
            assert bstree_0._root._right._left._left._lheight == 0
            assert bstree_0._root._right._left._left._rheight == 0

            assert bstree_0._root._right._left._left._left == None
            assert bstree_0._root._right._left._left._right == None

            assert bstree_0._root._right._left._right._value == 17
            assert bstree_0._root._right._left._right._lheight == 0
            assert bstree_0._root._right._left._right._rheight == 0

            assert bstree_0._root._right._left._right._left == None
            assert bstree_0._root._right._left._right._right == None

            assert bstree_0._root._right._right._value == 50
            assert bstree_0._root._right._right._lheight == 3
            assert bstree_0._root._right._right._rheight == 2

            assert bstree_0._root._right._right._right._value == 51
            assert bstree_0._root._right._right._right._lheight == 0
            assert bstree_0._root._right._right._right._rheight == 1

            assert bstree_0._root._right._right._right._right._value == 52
            assert bstree_0._root._right._right._right._right._lheight == 0
            assert bstree_0._root._right._right._right._right._rheight == 0

            assert bstree_0._root._right._right._left._value == 40
            assert bstree_0._root._right._right._left._lheight == 2
            assert bstree_0._root._right._right._left._rheight == 0

            assert bstree_0._root._right._right._left._right == None

            assert bstree_0._root._right._right._left._left._value == 36
            assert bstree_0._root._right._right._left._left._lheight == 1
            assert bstree_0._root._right._right._left._left._rheight == 1

            assert bstree_0._root._right._right._left._left._left._value == 35
            assert bstree_0._root._right._right._left._left._left._lheight == 0
            assert bstree_0._root._right._right._left._left._left._rheight == 0

            assert bstree_0._root._right._right._left._left._left._left == None
            assert bstree_0._root._right._right._left._left._left._right == None

            assert bstree_0._root._right._right._left._left._right._value == 37
            assert bstree_0._root._right._right._left._left._right._lheight == 0
            assert bstree_0._root._right._right._left._left._right._rheight == 0

            assert bstree_0._root._right._right._left._left._right._left == None
            assert bstree_0._root._right._right._left._left._right._left == None

    print('test_remove_node(): finished...')
