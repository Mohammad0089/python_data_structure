# To do a level-order traversal of a binary tree, we require a queue. 


class Queue(object): #first in first out
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data) # append will add elements to the last [10,9,1,....]
        
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise("Queue is Empty")
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        
    def __len__(self): #over riding len()
        return len(self.queue)
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.queue == list()
    
class Stack(object):
    def __init__(self):
        self.items = list()
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop() # pop and return the last element
        else:
            raise("stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]   #return the last element
        else:
            raise("stack is empty")
    
    def __len__(self):
        return len(self.items)
    
    def size (self):
        return len(self.items)
    
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
# my_queue = Queue()

# my_queue.enqueue("1st")
# my_queue.enqueue("2nd")
# my_queue.enqueue("3rd")
# my_queue.enqueue("4th")
# my_queue.enqueue("5th")
# print()
# print("queue is = {}\n".format(my_queue.queue))
# my_queue.dequeue() # deque first element 
# print("length is: {} isEmpty {} dequeue one element queue is: {}\n".format(my_queue.size() , my_queue.isEmpty() , my_queue.queue))
# print("the peek method will return the value of the last element: {}\n".format(my_queue.peek()))


# my_stack = Stack()
# my_stack.push("1st")
# my_stack.push("2nd")
# my_stack.push("3rd")
# my_stack.push("4th")
# my_stack.push("5th")

# print("my_stack is {}".format(my_stack.items))
# print("pop the last element: {}".format(my_stack.pop()))
# print("my_stack is {}".format(my_stack.items))
