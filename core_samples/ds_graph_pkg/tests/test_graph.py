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

def test_graph_struct(get_graph_list) -> None:
    print('test_graph_struct(): started...')

    for _graph, file in get_graph_list:
        if file == 'graph_1.json':
            assert _graph.is_cyclic() == True
        elif file == 'graph_2.json':
            assert _graph.is_cyclic() == False
        elif file == 'graph_3.json':
            assert _graph.is_cyclic() == False
        elif file == 'graph_4.json':
            assert _graph.is_cyclic() == True
        elif file == 'graph_5.json':
            assert _graph.is_cyclic() == True
        elif file == 'graph_6.json':
            assert _graph.is_cyclic() == True
        elif file == 'graph_7.json':
            assert _graph.is_cyclic() == True
        elif file == 'graph_8.json':
            assert _graph.is_cyclic() == True

    print('test_graph_struct(): finished...')


