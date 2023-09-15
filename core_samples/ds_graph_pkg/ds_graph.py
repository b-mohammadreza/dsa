#!/usr/bin/python

from typing import Self
import sys
sys.path.append('..')
from priority_queue.priority_queue import PriorityQueue

class GraphNode:
    def __init__(self, data: str) -> None:
        # for convenience I defined the data member as 'str',
        #  it could be any data structure to hold Node data
        self._data: str = data 

class GraphStruct:
    """ The data structure to define the gragh """

    # travese types
    T_TYPE_DFS = 0
    T_TYPE_BFS = 1

    # commands for updating the adjacency matrix
    _U_REMOVE = 0
    _U_ADD = 1

    # to determine shortest path algorithm
    SHORTEST_PATH_DIJKSTRA = 0
    SHORTEST_PATH_BELLMAN_FORD = 1

    def __init__(self, nodes: list[GraphNode], adj_matrix: list[list[int]]) -> None:
        self._adj_matrix = adj_matrix
        self._nodes = nodes

    def numberof_nodes(self) -> int:
        return len(self._nodes)

    def traverse(self, t_type) -> None:
        """ TODO: corner case: in case if there is a node
         which is not connected to others, need to initiate
         the traverse function on each node separately """

        if t_type == GraphStruct.T_TYPE_DFS:
            self._dfs(0, [], [])
        else:
            self._bfs(0)

    def _dfs(self, node_index: int, visited: list[int], stack: list[int]) -> bool:
        is_cyclic: bool = False

        if self._adj_matrix[node_index][node_index] > 0:
            is_cyclic = True

        if len(stack) > 2 and node_index != stack[-2] and node_index in stack:
            is_cyclic = True

        if node_index in visited:
            return is_cyclic

        visited.append(node_index)

        stack.append(node_index)

        adj_arr = self._adj_matrix[node_index]

        for index, val in enumerate(adj_arr):
            if val > 0:
                ret = self._dfs(index, visited=visited, stack=stack)
                if ret == True:
                    is_cyclic = True

        stack.pop()

        return is_cyclic

    def _bfs(self, start_index: int) -> None:
        visited: list[int] = []
        to_visit: list[int] = []

        to_visit.append(start_index)

        while len(to_visit) > 0:
            next_index = to_visit.pop(0)

            visited.append(next_index)

            adj_arr = self._adj_matrix[next_index]

            for index, val in enumerate(adj_arr):
                if val > 0 and index not in visited and index not in to_visit:
                    to_visit.append(index)



    def is_cyclic(self) -> bool:
        return self._dfs(0, [], [])

    def remove(self, val) -> (bool, Self):
        for index, node in enumerate(self._nodes):
            if node._data == val:
                self._nodes.pop(index)

                return self._update_graph(GraphStruct._U_REMOVE, index)

        return (False, None)
        
    def _update_graph_remove(self, index) -> (bool, Self):
        for row_index, _ in enumerate(self._adj_matrix):
            if row_index == index:
                self._adj_matrix.pop(index)
                break
        else:
            return (False, None) 

        for row in self._adj_matrix:
            for col_index, _ in enumerate(row):
                if col_index == index:
                    row.pop(index)
                    break
            else:
                """can't reach here because _adj_matrix is a square matrix"""
        
        return (True, self)


    def _update_graph(self, cmd, index) -> (bool, Self):
        match cmd:
            case GraphStruct._U_REMOVE:
                return self._update_graph_remove(index)
            case GraphStruct._U_ADD:
                return (False, None)
            case _:
                return (False, None)

    def shortest_paths(self, algo):
        """implements Dijkstra's or Bellman-Ford's algorithms"""

        if algo == GraphStruct.SHORTEST_PATH_DIJKSTRA:
            return self._dijkstra()
        
        return self._bellman_ford()

    def _dijkstra(self) -> list[int]:
        distances: list[int] = [sys.maxsize for _ in range(len(self._nodes))]   # O(n) time, O(n) space 
        unvisited: list[int] = [index for index in range(len(self._nodes))]     # O(n) time, O(n) space
        # in our implementation source node is always the first node
        distances[0] = 0

        while True:                                                             # iterate time: O(n)
            # following is a min heap of unvisited nodes distances
            p_queue = PriorityQueue()
            init_vals = [distances[index] for index in unvisited]               # O(n) time, O(n) space
            p_queue.heapify(init_vals)                                          # O(n log n) > time, space O(n)

            _, dist = p_queue.dequeue()                                         # O(log n) time, space = 0

            # expected no ValueError to be raised, because 'dist' value just
            # added to the 'distances' list 
            cur_index = distances.index(dist)                                   # O(n) time, space = 0

            # expected no ValueError to be raised, because the index selected from
            # existing values in 'unvisited' list 
            unvisited.remove(cur_index)                                         # O(n) time, space = 0
            if len(unvisited) < 1:
                break

            unvisited_neighbors = self._dijk_get_unvisitd_neighbors(cur_index=cur_index, unvisited=unvisited)   # O(n^2) time, space O(n)
            for index, weight in unvisited_neighbors:
                new_weight = dist + weight
                if new_weight < distances[index]:
                    distances[index] = new_weight

        return distances
            
    def _dijk_get_unvisitd_neighbors(self, cur_index, unvisited: list[int]) -> list[int]:
        neighbors = []
        for index, weight in enumerate(self._adj_matrix[cur_index]):
            if weight > 0 and index != cur_index:
                neighbors.append((index, weight))

        unvisited_neighbors = []
        for index, weight in neighbors:
            if index in unvisited:
                unvisited_neighbors.append((index, weight))

        return unvisited_neighbors

    def _bellman_ford(self) -> (list[int], list[int]):
        distances: list[int] = [sys.maxsize for _ in range(len(self._nodes))]   # O(n) space
        prev_list: list[int] = [None for _ in range(len(self._nodes))]          # O(n) space

        # in our implementation source node is always the first node
        distances[0] = 0

        for _ in range(len(self._nodes) - 1):                                   # O(V * E) time, V = number of vertices, E = number of edges
            for u_index, row in enumerate(self._adj_matrix):
                for v_index, weight in enumerate(row):
                    if weight > 0:
                        dist = distances[u_index] + weight
                        if dist < distances[v_index]:
                            distances[v_index] = dist
                            prev_list[v_index] = u_index

        return (distances, prev_list)

    def min_spanning_tree(self) -> None:
        """implements Kruskal's or Prim's algorithms"""
        pass

if __name__ == '__main__':
    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,1,1], [1,0,1,0], [1,1,0,0], [1,0,0,0]])

    # (result, new_graph) = graph.remove('abb')
    # print(f'>>>>result: {result}')
    # print(f'>>>>new_graph nodes: {new_graph._nodes}')
    # print(f'>>>>new_graph adj matrix: {new_graph._adj_matrix}')



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

    # graph.shortest_paths(GraphStruct.SHORTEST_PATH_DIJKSTRA)
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)

    # graph = GraphStruct([GraphNode('aaa'), GraphNode('aab'), GraphNode('abb'), GraphNode('bbb')]
    #                     , [[0,1,4,0], [0,0,2,5], [0,0,0,0], [0,0,0,0]])

    # graph.shortest_paths(GraphStruct.SHORTEST_PATH_BELLMAN_FORD)
    # print(f'is graph cyclic: {graph.is_cyclic()}')
    # graph.traverse(GraphStruct.T_TYPE_BFS)
    pass
