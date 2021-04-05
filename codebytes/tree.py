class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def preorder(self):

        def _print(current):
            if current:
                print("\t{}".format(current.data))
                _print(current.left) 
                _print(current.right)
        
        _print(self.root)

    def inorder(self):

        def _print(current):
            if current:
                _print(current.left)
                print("\t{}".format(current.data))
                _print(current.right)
        
        _print(self.root)

    def postorder(self):

        def _print(current):
            if current:
                _print(current.left)
                _print(current.right)
                print("\t{}".format(current.data))
        
        _print(self.root)
    
    def inorder_iterative(self):
        node = self.root
        q = []
        if node is None:
            return

        while True:
            if node:
                q.append(node)
                node = node.left
            else:
                if not q:
                    break
                else:
                    node = q.pop()
                    print("\t",node.data)
                    node=node.right
        return

    def preorder_iterative(self):
        node = self.root
        q = []
        if node is None:
            return
        q.append(node)
        
        while q:
            node = q.pop()
            print(node.data)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return

    def levelorder(self):

        result = []
        q = [self.root]
        if self.root:
            result.append("{}".format(self.root.data))
            result.append("\n")
        while q != []:
            current = q.pop(0)
            if current.left:
                q.append(current.left)
                result.append("\t{}".format(current.left.data))
            if current.right:
                q.append(current.right)
                result.append("\t{}".format(current.right.data))
            result.append("\n")
        print("".join(result))
        
    def insert(self, value):

        def _insert(root, value):
            current = root
            if value < current.data:
                if current.left:
                    _insert(current.left, value)
                else:
                    current.left = TreeNode(value)
            else:
                if current.right:
                    _insert(current.right, value)
                else:
                    current.right = TreeNode(value)

        if self.root:
            _insert(self.root, value)
        else:
            self.root = TreeNode(value)

    def delete(self):
        pass

    def _find(self, value):
        pass

    def successor(self, value):
        
        def _min(current):
            if not current:
                return None
            while current.left:
                current = current.left
            return current
    
        current = self.root
        prev = current
        search_path = []
        while current:
            if current.data == value:
                break
            else:
                search_path.append(current.data)
                prev = current
                if value < current.data:
                    current = current.left
                else:
                    current = current.right

        if current.right:
            return _min(current.right).data
        else:
            i = len(search_path)-1
            while i >= 0 and search_path[i] < value:
                i = i-1
            if i < 0:
                return None
            else:
                return search_path[i]

    def predecessor(self, value):
        
        def _max(current):
            if not current:
                return None
            while current.right:
                current = current.right
            return current
    
        current = self.root
        prev = current
        search_path = []
        while current:
            if current.data == value:
                break
            else:
                search_path.append(current.data)
                prev = current
                if value < current.data:
                    current = current.left
                else:
                    current = current.right

        if current.left:
            return _max(current.left).data
        else:
            i = len(search_path)-1
            while i >= 0 and search_path[i] > value:
                i = i-1
            if i < 0:
                return None
            else:
                return search_path[i]

    def min(self):
        current = self.root 
        if not current:
            return None
        while current.left:
            current = current.left
        return current

    def max(self):
        current = self.root 
        if not current:
            return None
        while current.right:
            current = current.right
        return current


if __name__ == "__main__":
    """
    T = Tree()
    T.inorder()
    print("#"*40)
    T.insert(33)
    T.inorder()
    print("#"*40)
    T.insert(44)
    T.inorder()
    print("#"*40)
    T.insert(11)
    T.inorder()
    print("#"*40)
    """

    T = Tree()
    T.insert(33)
    T.insert(66)
    T.insert(55)
    T.insert(44)
    T.insert(11)
    T.insert(99)
    T.insert(22)
    T.insert(77)
    T.insert(88)
    #T.levelorder()
    T.inorder()
    print("#"*40)
    T.inorder_iterative()
    print("#"*40)
    #print(T.max().data)
    #print(T.min().data)

    """
    for i in [11,22,33,44,55,66,77,88,99]:
        print(i,"h")
        print(T.successor(i))
        print(T.predecessor(i))

    
    ************33********
    ***11**************66***
    *******22*******55**********99
    *************44***********77
    *****************************88*****
    """


"""
do_exit = False
    if root:
        # print(root.val)
        count,do_exit_l= findSingleValueTrees_helper(root.left_ptr,count)
        count,do_exit_r= findSingleValueTrees_helper(root.right_ptr,count)
        do_exit = do_exit_l or do_exit_r
        
        if not do_exit:
            if (root.left_ptr == None and root.right_ptr == None):
                count = count + 1
            elif (root.left_ptr == None):
                if root.right_ptr.val == root.val:
                    count = count + 1
                else:
                    do_exit = True
            elif (root.right_ptr == None):
                if root.left_ptr.val == root.val:
                    count = count + 1
                else:
                    do_exit = True
            elif (root.left_ptr.val == root.val and root.right_ptr.val == root.val):
                count = count + 1
            else:
                do_exit = True
"""