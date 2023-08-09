#!/usr/bin/python

class TreeNode:
    def __init__(self) -> None:
        self.value = None
        self.left : TreeNode = None
        self.right : TreeNode = None

class TreeList:
    count : int = 0
    added = False
    currentId : int = 0
    targetNode: TreeNode = None

    def __init__(self, root) -> None:
        self.root : TreeNode = root
        self.init_count(self.root)
        print(f'TreeList: total nodes count: {TreeList.count}')

    def init_count(self, node: TreeNode) -> None:
        if node is None:
            return

        TreeList.count += 1
        self.init_count(node.left)
        self.init_count(node.right)

    def add_init(self) -> None:
        TreeList.currentId = 0
        TreeList.targetNode = None
        TreeList.added = False

    def add(self, val):
        self.add_init()
        self.add_impl(self.root, val)

    def search(self, val) -> bool:
        return self.dfs(val)

    def dfs(self, val) -> bool:
        return self.dfs_impl(self.root, val)

    def dfs_impl(self, node: TreeNode, val) -> bool:
        if node is None:
            return False
        
        if node.value == val:
            return True
        
        ret = self.dfs_impl(node.left, val)

        if ret == False:
            ret = self.dfs_impl(node.right, val)

        return ret
    

    def add_impl(self, node: TreeNode, val):
        if TreeList.added == True:
            return

        if node.left is None and node.right is None:
            TreeList.currentId += 1
            print(f'<<<<<TreeList.currentId: {TreeList.currentId}')

            if node is self.root:
                self.root.left = TreeNode()
                self.root.left.value = val
                TreeList.count += 1
                TreeList.added = True
                print(f'TreeList: adding to root.left. root val: {self.root.value}')
            elif TreeList.currentId >= TreeList.count:
                new_node = TreeNode()
                new_node.value = val
                TreeList.targetNode.left = new_node
                TreeList.count += 1
                TreeList.added = True
                print(f'TreeList: adding to the targetNode. parent val: {TreeList.targetNode.value}')
            return

        TreeList.currentId += 1
        print(f'>>>>TreeList.currentId: {TreeList.currentId}')

        if node.left is not None:
            self.add_impl(node.left, val)
        else:
            new_node = TreeNode()
            new_node.value = val
            node.left = new_node
            TreeList.count += 1
            TreeList.added = True
            print(f'TreeList: adding to the left. parent val: {node.value}')
            return

        if TreeList.added == True:
            return

        if TreeList.targetNode is None:
            TreeList.targetNode = node.left

        if node.right is not None:
            self.add_impl(node.right, val)
        else:
            new_node = TreeNode()
            new_node.value = val
            node.right = new_node
            TreeList.count += 1
            TreeList.added = True
            print(f'TreeList: adding to the right. parent val: {node.value}')
        return


def build_tree(init_list : list) -> (TreeNode, list):
    if len(init_list) < 1:
        return (None, init_list)
    if str(init_list[0]).lower() == 'x':
        return (None, init_list[1:])

    parent = TreeNode()

    parent.value = init_list[0]
    init_list = init_list[1:]

    (parent.left, init_list) = build_tree(init_list=init_list)
    (parent.right, init_list) = build_tree(init_list=init_list)

    return (parent, init_list)

if __name__ == '__main__':
    root,_ = build_tree([6, 3, 1, 'x', 'x', 'x', 2, 'x', 'x'])
    print(root.value)
    print(root.left.value)
    print(root.left.right)
    print(root.left.left.value)
    print(root.left.left.left)
    print(root.left.left.right)
    print(root.right.value)
    print(root.right.left)
    print(root.right.right)

    tree = TreeList(root)
    print(f'TreeList.currentId: {TreeList.currentId}')
    print(f'TreeList.count: {TreeList.count}')

    print('********* 1st add')
    tree.add(val=4)
    print(f'***** TreeList.currentId: {TreeList.currentId}')
    print(f'***** TreeList.count: {TreeList.count}')

    print('&&&&&&&&& 2nd add')
    tree.add(val=5)
    print(f'&&&& TreeList.currentId: {TreeList.currentId}')
    print(f'&&&& TreeList.count: {TreeList.count}')

    print(f'search 4: {tree.search(val=4)}')
    print(f'search 12: {tree.search(val=12)}')

    # root,_ = build_tree([6, 3, 'x', 'x', 2, 'x', 'x'])
    # print(root.value)
    # print(root.left.value)
    # print(root.left.left)
    # print(root.left.right)
    # print(root.right.value)
    # print(root.right.left)
    # print(root.right.right)

    # tree = TreeList(root)
    # print(f'TreeList.currentId: {TreeList.currentId}')
    # print(f'TreeList.count: {TreeList.count}')

    # print('********* 1st add')
    # tree.add(val=4)
    # print(f'***** TreeList.currentId: {TreeList.currentId}')
    # print(f'***** TreeList.count: {TreeList.count}')

    # print('&&&&&&&&& 2nd add')
    # tree.add(val=5)
    # print(f'&&&&& TreeList.currentId: {TreeList.currentId}')
    # print(f'&&&&& TreeList.count: {TreeList.count}')




