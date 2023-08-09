#!/usra/bin/python

class GraphNode:
    pass

class GraphStruct:
    T_TYPE_DFS = 0
    T_TYPE_BFS = 1

    def __init__(self, adj_matrix: list) -> None:
        self.adjMatrix = adj_matrix

    def traverse(self, t_type) -> None:
        if t_type == GraphStruct.T_TYPE_DFS:
            return self.__dfs()
        return self.__bfs()

    def shortest_path(self) -> None:
        """implement both Dijkstra's andBellman-Ford's algorithms"""
        pass

    def min_spanning_tree(self) -> None:
        """implement both Kruskal's and Prim's algorithms"""
        pass

    def __dfs(self) -> None:
        pass

    def __bfs(self) -> None:
        pass

    def is_cyclic(self) -> bool:
        pass

    def remove(self, val) -> bool:
        pass

    def __update_adj_matrix(self) -> None:
        pass

def build_graph(adj_matrix: list) -> None:
    pass

if __name__ == '__main__':
    pass