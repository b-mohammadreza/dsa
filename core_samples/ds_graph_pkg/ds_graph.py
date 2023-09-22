#!/usr/bin/python

from typing import Self
import sys
sys.path.append('..')

from priority_queue.priority_queue import PriorityQueue
from merge_sort.merge_sort import msort
from disjoint_set_union.dsu import DisjointSetUnion

class EdgeInfo:
    def __init__(self, edge: tuple, weight: int) -> None:
        self._edge = edge
        self._weight = weight

    def __lt__(self, other: Self):
        return self._weight < other._weight

    def __le__(self, other: Self):
        return self._weight <= other._weight
    
    def __eq__(self, other: Self):
        if self._edge == other._edge and self._weight == other._weight:
            return True

        if      self._edge[0] == other._edge[1] \
            and self._edge[1] == other._edge[0] \
            and self._weight  == other._weight:
            return True
        
        return False
        

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

    # to determine minimum spanning tree algorithm
    MIN_SPAN_KRUSKAL = 0
    MIN_SPAN_PRIM = 1

    def __init__(self, nodes: list[GraphNode], adj_matrix: list[list[int]]) -> None:
        self._adj_matrix = adj_matrix
        self._nodes = nodes

    def numberof_nodes(self) -> int:
        return len(self._nodes)

    def traverse(self, t_type) -> None:
        """ TODO: corner case: in case if there is a node
         which is not connected to others, need to initiate
         the traverse function on each node separately """

        if t_type == self.T_TYPE_DFS:
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

                return self._update_graph(self._U_REMOVE, index)

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
            case self._U_REMOVE:
                return self._update_graph_remove(index)
            case self._U_ADD:
                return (False, None)
            case _:
                return (False, None)

    def shortest_paths(self, algo):
        """implements Dijkstra's or Bellman-Ford's algorithms"""

        if algo == self.SHORTEST_PATH_DIJKSTRA:
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

    def min_spanning_tree(self, algorithm) -> list[tuple]:
        """implements Kruskal's or Prim's algorithms"""
        if algorithm == self.MIN_SPAN_KRUSKAL:
            return self._kruskal()
        
        return self._prim()

    def _get_edge_infos_kruskal(self) -> list[EdgeInfo]:
        edge_infos: list[EdgeInfo] = []

        for index_1, weights in enumerate(self._adj_matrix):
            for index_2, weight in enumerate(weights):
                if weight > 0:
                    edge_info = EdgeInfo(edge=(index_1, index_2), weight=weight)

                    if edge_info not in edge_infos:
                        edge_infos.append(edge_info)

        return edge_infos

    def _kruskal(self) -> list[tuple]:
        """ Each graph edge is represented by a tuple: (index_1, index_2),
        in which 'index_1' is the index of 1st node and 'index_2' is the index
        of the 2nd node. """

        print(f'Get Minimum Spanning Tree using the Kruskal\'s algorithm...')

        min_span_tree: list[tuple] = []
        edge_infos: list[EdgeInfo] = self._get_edge_infos_kruskal()                     # O(n^2)

        sorted_edge_infos = msort(edge_infos)                                   # O(E log E)

        # Initializing a Disjoint Set Union data structure to detect
        # a cylce after traversing each edge
        dsu_obj = DisjointSetUnion(range(len(self._adj_matrix)))

        edge_info: EdgeInfo
        for edge_info in sorted_edge_infos:                                     # O(n)
            if len(min_span_tree) == self.numberof_nodes() - 1:
                break

            try:
                (result, _, set_id_1) = dsu_obj.find(edge_info._edge[0])        # O(n)
                if result == False:
                    raise ValueError

                (result, _, set_id_2) = dsu_obj.find(edge_info._edge[-1])       # O(n)
                if result == False:
                    raise ValueError
                
                if set_id_1 == set_id_2:
                    print(f'_kruskal(): cycle detected when processing the\
                    ({edge_info._edge[0]},{edge_info._edge[-1]}) edge.')
                else:
                    dsu_obj.union(edge_info._edge[0], edge_info._edge[-1])      # O(n)
                    min_span_tree.append(edge_info._edge)

            except ValueError as e:
                print(f'_kruskal(): one of the ({edge_info._edge[0]} or {edge_info._edge[-1]})\
                       nodes not found in DSU.')
                
        return min_span_tree

    def _get_edge_infos_prim(self, u: int, v_set: set[int]) -> list[EdgeInfo]:
        edge_infos: list[EdgeInfo] = []

        for v, weight in enumerate(self._adj_matrix[u]):
            if weight > 0 and v not in v_set:
                edge_infos.append(EdgeInfo((u,v), weight))
                # print(f'>>>> edge: {edge_infos[-1]._edge}, weight: {edge_infos[-1]._weight}')

        return edge_infos

    def _prim(self) -> list[tuple]:
        print(f'Get Minimum Spanning Tree using the Prim\'s algorithm...')

        min_span_tree: list[tuple] = []
        vertices: list[int] = range(len(self._adj_matrix))
        v_set: set[int] = {vertices[0]}

        vertex = vertices[0]
        min_heap = PriorityQueue()

        while len(v_set) < len(vertices):                                                   # O(V * V)
            edge_infos: list[EdgeInfo] = self._get_edge_infos_prim(vertex, v_set)           # O(V)

            for edge_info in edge_infos:
                min_heap.enqueue(edge_info)                                                 # O(log E)

            while True:
                (_, edge_info) = min_heap.dequeue()                                         # O(V) max?
                if edge_info is None:
                    break

                vertex = edge_info._edge[1]
                if vertex not in v_set:
                    break

            min_span_tree.append(edge_info._edge)
            v_set.add(vertex)

        return min_span_tree

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
