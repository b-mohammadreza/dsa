from .. import priority_queue
import pytest
import json
import os

@pytest.fixture
def get_file_list() -> list[str]:
    return os.listdir('test/arrays')

@pytest.fixture
def get_array_list(get_file_list) -> list[(list[int], str)]:
    arr_file_list = []

    if len(get_file_list) < 1:
        raise ValueError('get_graph_list(): no test-case files found...')

    for json_file in get_file_list: 
        with open(f'test/arrays/{json_file}', 'r') as fstr:
            file_data = json.load(fstr)
        arr_file_list.append((file_data['arr'], json_file))
    
    return arr_file_list

def test_heapify(get_array_list) -> None:
    print('test_heapify(): started...')

    for arr, file_name in get_array_list:
        # print(f'test_heapify(): arr -> {arr}')
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            assert min_heap_1.heapify(arr) == [7,19,8,33,25,10,55,41]
        # elif file_name == 'arr_2.json':
        #     min_heap_2 = priority_queue.PriorityQueue()
        #     assert min_heap_2.heapify(arr) == [3,12,5,18]
        # elif file_name == 'arr_3.json':
        #     min_heap_3 = priority_queue.PriorityQueue()
        #     assert min_heap_3.heapify(arr) == [2,25,5,31,30,7,11,100,40,40,50,20,61,13,17]

    print('test_heapify(): finished...')

# def test_enqueue(get_array_list) -> None:
#     print('test_enqueue(): started...')

#     for arr, file_name in get_array_list:
#         if file_name == 'arr_1.json':
#             pass
#         elif file_name == 'arr_2.json':
#             pass
#         elif file_name == 'arr_3.json':
#             pass

#     print('test_enqueue(): finished...')

# def test_dequeue(get_array_list) -> None:
#     print('test_dequeue(): started...')

#     for arr, file_name in get_array_list:
#         if file_name == 'arr_1.json':
#             pass
#         elif file_name == 'arr_2.json':
#             pass
#         elif file_name == 'arr_3.json':
#             pass

#     print('test_dequeue(): finished...')

# def test_peek(get_array_list) -> None:
#     print('test_peek(): started...')

#     for arr, file_name in get_array_list:
#         if file_name == 'arr_1.json':
#             pass
#         elif file_name == 'arr_2.json':
#             pass
#         elif file_name == 'arr_3.json':
#             pass

#     print('test_peek(): finished...')
