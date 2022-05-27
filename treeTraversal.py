
from queueAndstack import Queue, Stack

class Node(object):
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self,root):
        self.root = Node(root)
    
    def print_tree(self,type):
        if type == "pre":
            return self.pre_order_print(self.root,"")
        elif type == "in":
            return self.in_order_print(self.root,"")
        elif type == "post":
            return self.post_order_print(self.root,"")
        elif type == "top":
            return self.top_level_order_print()
        elif type == "bottom":
            return self.bottom_order_print()
        else:
            raise("this type {} is not supported, supported types are: pre, in, post,top, and bottom".format(type))
    def pre_order_print(self, start, traversal):
        
        "root->left->right"
        if start:
            traversal += str(start.data) + "-"
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal  
    def in_order_print(self, start, traversal):
        "left->root->right"
        if start: 
            traversal = self.in_order_print(start.left,traversal)
            traversal += str(start.data) + "-"
            traversal = self.in_order_print(start.right, traversal)
        return traversal
    
    def post_order_print(self,start,traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal+= str(start.data) + "-"
        return traversal
    def top_level_order_print(self):
        start = self.root
        traversal= ""
        my_queue = Queue() 
        my_queue.enqueue(start)
        while len(my_queue)>0:
            traversal += str(my_queue.peek().data) + "-"
            node = my_queue.dequeue()
            if node.left:
                my_queue.enqueue(node.left)
            if node.right:
                my_queue.enqueue(node.right)
        return traversal
    def bottom_order_print(self):
        my_stack = Stack()
        my_queue = Queue()
        traversal = ""
        start = self.root
        my_queue.enqueue(start)
        
        while len(my_queue)>0:
            
            node = my_queue.dequeue()
            my_stack.push(node)
                        
            if node.left:
                my_queue.enqueue(node.left)
            if node.right:
                my_queue.enqueue(node.right)
                
        while my_stack.size()>0:
            traversal+=str(my_stack.pop().data) + "-"
            
        return traversal
    def tree_hight(self):
        node = self.root
        def _hight(node):
            if node is None:
                return -1
            left_hight = _hight(node.left)  
            right_hight = _hight(node.right)
            return 1 + max(left_hight,right_hight)

        return _hight(node)
    
    def height_1(self):
        def _height(node):
            if node is None:
                return -1
            left = _height(node.left) + 1
            right = _height(node.right) + 1
            
            return max (left , right)
        return _height(self.root)
    def size(self):
        start = self.root
        def _size(node):
            if node is None:
                return 0
            return _size(node.left) + _size(node.right) + 1
        return _size(start)
    def size_1(self): #iterative way
        start = self.root
        my_stack = Stack()
        my_stack.push(start)
        count = 0
        while my_stack:
            node = my_stack.pop()
            count +=1
            if node.left:
                my_stack.push(node.left) 
            if node.right:
                my_stack.push(node.right)
              
        return count
        
            
        
         
my_tree = Tree(10)

my_tree.root.left = Node(9)
my_tree.root.right = Node(8)

my_tree.root.left.left = Node(7)
my_tree.root.left.right = Node(6)

my_tree.root.right.left = Node(5)
my_tree.root.right.right = Node(4)
my_tree.root.right.right.right = Node(1)


# 10-9-7-6-8-5-4- pre_order
# 7-9-6-10-5-8-4- in_order
# 7-6-9-5-4-8-10- post_order

#               10
#           /        \  
#          9          8  
#         /  \      /   \
#        7    6    5     4
#                         \
#                           1

print("""
              10
          /        \  
         9          8  
        /  \      /   \\
       7    6    5     4 
                        \\
                          1
    """)

print()
preOrder= my_tree.print_tree("pre")
print("pre_order tree traversal: {}\n".format(preOrder))

inOrder = my_tree.print_tree("in")
print("in_order tree traversal: {}\n".format(inOrder))

postOrder = my_tree.print_tree("post")
print("post_order tree traversal: {}\n".format(postOrder))

same_level = my_tree.print_tree("top")
print("top_level_order tree traversal: {}\n".format(same_level))

bottom_top_level_traversal = my_tree.print_tree("bottom")
print("bottom_level_order_print: {}\n".format(bottom_top_level_traversal))

print("Hight of the tree is {}\n".format(my_tree.tree_hight()))

print("Hight of the tree is new height {}\n".format(my_tree.height_1()))

print("number of leaves (nodes) in the tree is {}\n".format(my_tree.size()))

print("number of leaves (nodes) in the tree is {} iterative way\n".format(my_tree.size_1()))



