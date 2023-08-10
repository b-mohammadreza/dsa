#!/usr/bin/python

class GraphNode:
    def __init__(self, data: str) -> None:
        # for convenience I defined the data member as 'str',
        #  it could be any data structure to hold Node data
        self._data: str = data 

class GraphStruct:
    T_TYPE_DFS = 0
    T_TYPE_BFS = 1

    def __init__(self, nodes: list[GraphNode], adj_matrix: list[list[int]]) -> None:
        self._adj_matrix = adj_matrix
        self._nodes = nodes

    def traverse(self, t_type) -> None:
        if t_type == GraphStruct.T_TYPE_DFS:
            return self._dfs(0, [])
        return self._bfs()

    def shortest_path(self) -> None:
        """implement both Dijkstra's andBellman-Ford's algorithms"""
        pass

    def min_spanning_tree(self) -> None:
        """implement both Kruskal's and Prim's algorithms"""
        pass

    def _dfs(self, node_index: int, visited: list[int]) -> None:
        if node_index in visited:
            print(f'GraphStruct_dfs(): node already visited - index: {node_index}')
            return

        print(f'GraphStruct_dfs(): >>>>>>>>>>node traversed - index: {node_index}, data: {self._nodes[node_index]._data}')
        visited.append(node_index)

        adj_arr = self._adj_matrix[node_index]
        print(f'GraphStruct_dfs(): **********adjucent nodes for node-{node_index}: {adj_arr}')

        for index in range(0, len(adj_arr)):
            if index > 0:
                self._dfs(index, visited=visited)

    def _bfs(self) -> None:
        pass

    def is_cyclic(self) -> bool:
        pass

    def remove(self, val) -> bool:
        pass

    def _update_graph(self) -> None:
        pass

def build_graph(adj_matrix: list) -> None:
    pass

if __name__ == '__main__':
    graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
                        , [[0,1,1,1], [1,0,1,0], [1,1,0,0], [1,0,0,0]])
    
    graph.traverse(GraphStruct.T_TYPE_DFS)
