# problem 1
# Happy Number
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1
# are happy. Return TRUE if n. is a happy number, and FALSE if not.

def is_happy_number(n):
    slow_pointer = n
    fast_pointer = number_to_squar_sum(n)
    print(f"slow_p = {slow_pointer}  fast_p = {fast_pointer}")
    
    while fast_pointer!=0 and fast_pointer !=slow_pointer:
         slow_pointer = number_to_squar_sum(slow_pointer)
         fast_pointer = number_to_squar_sum(number_to_squar_sum((fast_pointer)))      
    if fast_pointer == 1:
        return True
    return False

def number_to_squar_sum(n:int)->int:    #Helper function
    number=0
    while n != 0:
        number = number + (n % 10) **2
        n = n//10
    return number

# problem 2
# Check if a linked list contains a cycle or not. If a cycle exists, return TRUE. Otherwise, return FALSE.


def detect_cycle(head):

   head_1 = head

   slow_pointer = head_1
   fast_pointer = head_1.next
   
   while fast_pointer != slow_pointer and fast_pointer != None:
      slow_pointer = slow_pointer.next
      return True
   return False

# problem 3
# Circular Array Loop
def circular_array_loop(arr):  
    slow_p = 0
    fast_p = arr[0]
    size = len(arr) - 1
    
    while slow_p <= size:
        while slow_p != fast_p and is_dir_same(arr[slow_p], fast_p):
            if not is_dir_same(arr[fast_p], fast_p):
                return False
            fast_p = arr[fast_p] + fast_p
            if fast_p >= size or fast_p <= -size: # -size to cover cases that we circile with sum of negetive numbers
                fast_p = fast_p % size
        if fast_p == slow_p:
            return True
        slow_p += 1
    return False

def is_dir_same  (a , b)->bool:
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return True
    return False

print(circular_array_loop([-1,-1,-1,-1,-1]))

# problem 4 
# finding middle of the linklist

# Time complexity O(N)
# Space complexity O(1)

def get_middle_link(head):
    slow_p = head
    fast_p = head
    while fast_p and fast_p.next:
        
        fast_p = fast_p.next.next
        slow_p = slow_p.next
        
    return slow_p.data
