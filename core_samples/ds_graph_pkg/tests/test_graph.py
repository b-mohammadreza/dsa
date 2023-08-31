from .. import ds_graph
import pytest
import json
import os

def as_graph_struct(struct) -> ds_graph.GraphStruct:
    graph_nodes: list[ds_graph.GraphNode] = []
    graph_adj_mat: list[list[int]] = []

    try:
        val_list = struct['nodes']
        graph_nodes = [ds_graph.GraphNode(val) for val in val_list]
    except ValueError as e:
        print(f'as_graph_struct(): "nodes" attribute missed: {e}')

    try:
        graph_adj_mat = struct['adj_matrix']
    except ValueError as e:
        print(f'as_graph_struct(): "adj_matrix" attribute missed: {e}')

    return ds_graph.GraphStruct(graph_nodes, graph_adj_mat)

@pytest.fixture
def get_file_list() -> list[str]:
    return os.listdir('tests/graphs')

@pytest.fixture
def get_graph_list(get_file_list) -> list[(ds_graph.GraphStruct, str)]:
    graph_file_list = []

    if len(get_file_list) < 1:
        raise ValueError('get_graph_list(): no test file in "tests" dir...')

    for json_file in get_file_list: 
        with open(f'tests/graphs/{json_file}', 'r') as fstr:
            struct: ds_graph.GraphStruct = json.load(fstr, object_hook=as_graph_struct)
        graph_file_list.append((struct, json_file))
    
    return graph_file_list

def test_graph_is_cyclic(get_graph_list) -> None:
    print('test_graph_is_cyclic(): started...')

    for _graph, file_name in get_graph_list:
        if file_name == 'graph_1.json':
            assert _graph.is_cyclic() == True
        elif file_name == 'graph_2.json':
            assert _graph.is_cyclic() == False
        elif file_name == 'graph_3.json':
            assert _graph.is_cyclic() == False
        elif file_name == 'graph_4.json':
            assert _graph.is_cyclic() == True
        elif file_name == 'graph_5.json':
            assert _graph.is_cyclic() == True
        elif file_name == 'graph_6.json':
            assert _graph.is_cyclic() == True
        elif file_name == 'graph_7.json':
            assert _graph.is_cyclic() == True
        elif file_name == 'graph_8.json':
            assert _graph.is_cyclic() == True

    print('test_graph_is_cyclic(): finished...')


def test_graph_remove(get_graph_list) -> None:
    print('test_graph_remove(): started...')

    for _graph, file_name in get_graph_list:
        if file_name == 'graph_1.json':
            (result, new_graph) =  _graph.remove('abb')
            assert result == True
            assert new_graph._nodes[0]._data == "aaa"
            assert new_graph._nodes[1]._data == "aab"
            assert new_graph._nodes[2]._data == "bbb"
            assert new_graph._adj_matrix[0] == [0,1,1]
            assert new_graph._adj_matrix[1] == [1,0,0]
            assert new_graph._adj_matrix[2] == [1,0,0]

    print('test_graph_remove(): finished...')

def test_dijkstra(get_graph_list) -> None:
    print('test_dijkstra(): started...')

    for _graph, file_name in get_graph_list:
        if file_name == 'graph_9.json':
            distances = _graph.shortest_paths(ds_graph.GraphStruct.SHORTEST_PATH_DIJKSTRA)
            assert distances[0] == 0
            assert distances[1] == 2
            assert distances[2] == 3
            assert distances[3] == 1

    print('test_dijkstra(): finished...')
