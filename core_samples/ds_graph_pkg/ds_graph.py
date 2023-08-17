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
        """ TODO: corner case: in case if there is a node
         which is not connected to others, need to initiate
         the traverse function on each node separately """

        if t_type == GraphStruct.T_TYPE_DFS:
            self._dfs(0, [], [])
        else:
            self._bfs(0)

    def shortest_path(self) -> None:
        """implement both Dijkstra's andBellman-Ford's algorithms"""
        pass

    def min_spanning_tree(self) -> None:
        """implement both Kruskal's and Prim's algorithms"""
        pass

    def _dfs(self, node_index: int, visited: list[int], stack: list[int]) -> bool:
        is_cyclic: bool = False

        if self._adj_matrix[node_index][node_index] > 0:
            is_cyclic = True
            print(f'GraphStruct_dfs(): ^^node self cycle found-index: {node_index}')

        if len(stack) > 2 and node_index != stack[-2] and node_index in stack:
            is_cyclic = True
            print(f'GraphStruct_dfs(): ^^stack cycle found: {stack}')

        if node_index in visited:
            print(f'GraphStruct_dfs(): node already visited - index: {node_index}')
            return is_cyclic

        print(f'GraphStruct_dfs(): >>>>>>>>>>node traversed - index: {node_index}, data: {self._nodes[node_index]._data}')
        visited.append(node_index)

        stack.append(node_index)
        print(f'GraphStruct_dfs(): ^^stack push(): {stack}')

        adj_arr = self._adj_matrix[node_index]
        print(f'GraphStruct_dfs(): **********adjucent nodes for node-{node_index}: {adj_arr}')

        for index, val in enumerate(adj_arr):
            if val > 0:
                ret = self._dfs(index, visited=visited, stack=stack)
                if ret == True:
                    is_cyclic = True

        stack.pop()
        print(f'GraphStruct_dfs(): ^^stack pop(): {stack}')

        return is_cyclic

    def _bfs(self, start_index: int) -> None:
        visited: list[int] = []
        to_visit: list[int] = []

        to_visit.append(start_index)

        while len(to_visit) > 0:
            next_index = to_visit.pop(0)
            print(f'GraphStruct_bfs(): >>>>>>>>>>node traversed - index: {next_index}, data: {self._nodes[next_index]._data}')

            visited.append(next_index)

            adj_arr = self._adj_matrix[next_index]
            print(f'GraphStruct_bfs(): **********adjucent nodes for node-{next_index}: {adj_arr}')

            for index, val in enumerate(adj_arr):
                if val > 0 and index not in visited and index not in to_visit:
                    to_visit.append(index)
                    print(f'GraphStruct_bfs(): node-{index} added into "t_visit" list')



    def is_cyclic(self) -> bool:
        print('is_cyclic() called...')
        return self._dfs(0, [], [])

    def remove(self, val) -> bool:
        pass

    def _update_graph(self) -> None:
        pass

if __name__ == '__main__':
    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,1,1], [1,0,1,0], [1,1,0,0], [1,0,0,0]])
    
    # graph.traverse(GraphStruct.T_TYPE_DFS)
    # graph.traverse(GraphStruct.T_TYPE_BFS)
    # print(f'is graph cyclic: {graph.is_cyclic()}')

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,0,1], [1,0,1,0], [0,1,0,0], [1,0,0,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,0,0], [1,0,1,0], [0,1,0,1], [0,0,1,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,1,1], [1,0,1,1], [1,1,0,1], [1,1,1,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,0,0], [1,0,1,0], [0,1,1,1], [0,0,1,0]])
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)
    pass
