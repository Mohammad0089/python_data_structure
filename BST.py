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
            

        