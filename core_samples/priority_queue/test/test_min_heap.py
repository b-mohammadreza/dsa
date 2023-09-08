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
        raise ValueError('get_array_list(): no test-case files found...')

    for json_file in get_file_list: 
        with open(f'test/arrays/{json_file}', 'r') as fstr:
            file_data = json.load(fstr)
        arr_file_list.append((file_data['arr'], json_file))
    
    return arr_file_list

def test_is_min_heap(get_array_list) -> None:
    print('test_is_min_heap(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            assert min_heap_1.is_min_heap(arr) == False
        elif file_name == 'arr_2.json':
            min_heap_2 = priority_queue.PriorityQueue()
            assert min_heap_2.is_min_heap(arr) == False
        elif file_name == 'arr_3.json':
            min_heap_3 = priority_queue.PriorityQueue()
            assert min_heap_3.is_min_heap(arr) == False
        elif file_name == 'arr_4.json':
            min_heap_4 = priority_queue.PriorityQueue()
            assert min_heap_4.is_min_heap(arr) == True

    print('test_is_min_heap(): finished...')

def test_heapify(get_array_list) -> None:
    print('test_heapify(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            min_heap_1.heapify(arr)
            assert min_heap_1.is_min_heap() == True

        elif file_name == 'arr_2.json':
            min_heap_2 = priority_queue.PriorityQueue()
            min_heap_2.heapify(arr)
            assert min_heap_2.is_min_heap() == True

        elif file_name == 'arr_3.json':
            min_heap_3 = priority_queue.PriorityQueue()
            min_heap_3.heapify(arr)
            assert min_heap_3.is_min_heap() == True

    print('test_heapify(): finished...')

def test_enqueue(get_array_list) -> None:
    print('test_enqueue(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            min_heap_1.heapify(arr)
            min_heap_1.enqueue(priority=5)
            assert min_heap_1.is_min_heap() == True

        elif file_name == 'arr_2.json':
            min_heap_2 = priority_queue.PriorityQueue()
            min_heap_2.heapify(arr)
            min_heap_2.enqueue(priority=0)
            assert min_heap_2.is_min_heap() == True

        elif file_name == 'arr_3.json':
            min_heap_3 = priority_queue.PriorityQueue()
            min_heap_3.heapify(arr)
            min_heap_3.enqueue(priority=18)
            assert min_heap_3.is_min_heap() == True

    print('test_enqueue(): finished...')

def test_dequeue(get_array_list) -> None:
    print('test_dequeue(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            min_heap_1.heapify(arr)
            min_heap_1.dequeue()
            assert min_heap_1.is_min_heap() == True

        elif file_name == 'arr_2.json':
            min_heap_2 = priority_queue.PriorityQueue()
            min_heap_2.heapify(arr)
            min_heap_2.dequeue()
            assert min_heap_2.is_min_heap() == True

        elif file_name == 'arr_3.json':
            min_heap_3 = priority_queue.PriorityQueue()
            min_heap_3.heapify(arr)
            min_heap_3.dequeue()
            assert min_heap_3.is_min_heap() == True

    print('test_dequeue(): finished...')

def test_peek(get_array_list) -> None:
    print('test_peek(): started...')

    for arr, file_name in get_array_list:
        if file_name == 'arr_1.json':
            min_heap_1 = priority_queue.PriorityQueue()
            min_heap_1.heapify(arr)
            assert min_heap_1.peek() == 7

        elif file_name == 'arr_2.json':
            min_heap_2 = priority_queue.PriorityQueue()
            min_heap_2.heapify(arr)
            assert min_heap_2.peek() == 3

        elif file_name == 'arr_3.json':
            min_heap_3 = priority_queue.PriorityQueue()
            min_heap_3.heapify(arr)
            assert min_heap_3.peek() == 2

    print('test_peek(): finished...')
