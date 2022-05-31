class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val): 
        if self.root is None:
                self.root = Node(val)
        else:
            def _insert(node, data):
                
                if data < node.data:# data is smaller so goes to left 
                    if node.left:
                        _insert(node.left , data)
                    else:
                        node.left = Node(data)
                else:
                    if node.right: # data is greater or equal go right
                        _insert(node.right, data)
                    else:
                        node.right = Node(data)
            _insert(self.root, val)
    def find(self,target):
        def _find(node,val):
            if node:
                if node.data == val:
                    return True
                elif node.data > val:
                    return _find(node.left,val)
                else:
                    return _find(node.right,val)
            else:
                return False
        return _find(self.root, target)    

    def is_bst(self):
        def _is_bst(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.data
            if val<=lower or val>=upper:
                return False
            if not _is_bst(node.right, val, upper):
                return False
            if not _is_bst(node.left,lower, val):
                return False
            return True
        return _is_bst(self.root)
    
                
tree_bst = BST()

tree_bst.insert(8)
tree_bst.insert(3)
tree_bst.insert(10)
tree_bst.insert(1)
tree_bst.insert(6)
tree_bst.insert(9)
tree_bst.insert(11)
rt= tree_bst.root

print("                   {}\n\n".format(rt.data))
print("       {}                      {}\n\n".format(rt.left.data , rt.right.data))
print(" {}         {}           {}            {}\n\n".format(rt.left.left.data,rt.left.right.data , rt.right.left.data ,  rt.right.right.data))
            

print(tree_bst.find(8))
print(tree_bst.is_bst())