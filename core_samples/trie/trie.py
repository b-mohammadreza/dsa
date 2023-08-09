#!/usr/bin/python

class TrieNode:
    def __init__(self) -> None:
        self.value: str = ''
        self.children : dict[str, TrieNode] = {}
        self.isComplete : bool = False


class TrieStruct:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()
        self.root.isComplete = True

    def insert(self, key: str) -> TrieNode:
        return self.__insert_impl(self.root, key)

    def __insert_impl(self, node: TrieNode, key: str, index: int = 0) -> TrieNode:
        if index > len(key) or node is None:
            return None

        if index == len(key):
            node.isComplete = True
            return node

        next_node = node.children.get(key[index])

        if next_node is None:
            node.children[key[index]] = TrieNode()
            next_node = node.children[key[index]]
            next_node.value = key[index]
        
        return self.__insert_impl(next_node, key, index+1)

    def search(self, key: str) -> bool:
        return self.__search_impl(self.root, key)

    def __search_impl(self, node: TrieNode, key: str, index: int = 0):
        if index > len(key) or node is None:
            return False

        if index == len(key):
            return node.isComplete
        
        return self.__search_impl(node.children.get(key[index]), key, index+1)

    def delete(self) -> None:
        pass


if __name__ == '__main__':
    trie = TrieStruct()
    print(f'str("") found: {trie.search("")}')
    trie.insert('ab')
    print(f'str("ab") found: {trie.search("ab")}')
    print(f'str("a") found: {trie.search("a")}')
    print(f'str("b") found: {trie.search("b")}')
