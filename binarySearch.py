# binary search iterativ
def binary_search(data, target)->bool:
    low = 0
    high = len(data) - 1
    while low <=high:
        
        mid = (low + high)//2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1
    return False

# binary search recursivly
def binary_search_recursive(data, target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            return binary_search_recursive(data,target,mid+1,high)
        else:
            return binary_search_recursive(data,target,low,mid-1)    

# data = [1,3,4,8,9,12,14,18,22,85]
# res  =  binary_search_recursive(data , 12,0,len(data) - 1)
# print(res)

def find_nearest_number(array_a, target)-> int or None:
    """ This func to be used to find the nearest int within the list of integeres to the target integer.
    for this func to work properley, list must be sorted

    Args:
        array_a (int): list of integer
        target (int): Target Integer 

    Returns:
        int or None: if the array is empty None will be returned otherwise nearest integer to target 
    """
    size = len(array_a)
    #checking for edge cases 
    if size == 0:
        return None
    elif size == 1:
        return array_a[0]
    else:
        min_diff = min_diff_left = min_diff_right = float('inf')
        nearest_number = None
        lower_bound = 0
        upper_bound = size - 1
        
        while lower_bound <= upper_bound:
            
            mid_point = (lower_bound + upper_bound) // 2
            
            # checking to not read data out of bound 
            if mid_point + 1 < size:
                min_diff_right = abs(array_a[mid_point + 1] - target )
            if mid_point > 0:
                min_diff_left = abs(array_a[mid_point-1] - target)
            
            # finding the nearst numebr and min_diff      
            if min_diff_left < min_diff:
                min_diff = min_diff_left
                nearest_number = array_a[mid_point - 1]
            if min_diff_right < min_diff:
                min_diff = min_diff_right
                nearest_number = array_a[mid_point + 1]
            
            # Move the mid_point apporpiately as is done via binary search 
            if array_a[mid_point] < target:
                lower_bound = mid_point + 1
            elif array_a[mid_point] > target:
                upper_bound = mid_point - 1       
            else:
                return array_a[mid_point]
    return nearest_number
            

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
print("\nThe nearest number to: {} in the list {} is: {}\n".format(11, A1,find_nearest_number(A1, 11)))
print("The nearest number to: {} in the list {} is: {}\n".format(7, A1,find_nearest_number(A1, 7)))
print("The nearest number to: {} in the list {} is: {}\n".format(4 , A2,find_nearest_number(A2, 4)))
print("The nearest number to: {} in the list {} is: {}\n".format(7 , A2,find_nearest_number(A2, 7)))

def find_fix_point(A)-> None or int:
    # fix point means that A[i] == i
    # pre_conditions are: 1) list is sorted 2) elements are distinct
    
    #test edge case
    size = len(A)
    if size == 0:
        return None
    else:
        lower_bound = 0 
        upper_bound = size - 1
        
        while lower_bound <= upper_bound:
            mid_point = (lower_bound + upper_bound) // 2  
            if A[mid_point] < mid_point:      # since the list is sorted asending order, and elements are distinct,
                lower_bound = mid_point + 1   # so if elements before A[mid_point] are less than mid_point so there is no i where A[i] == i (every other element is off) [-5,-4,1,2...]  
            elif A[mid_point] > mid_point:    # in above case if 2 is mid_point which is at pos 3 we can gruntee that for every element before 2 A[i] != i  
                upper_bound = mid_point - 1
            else:
                return A[mid_point]
        return None
        
    
A1 = [-10, -5, 0, 3, 7] # Fixed point is 3
    
A2 = [0, 2, 5, 8, 17]  # Fixed point is 0
   
A3 = [-10, -5, 3, 4, 7, 9]  # No fixed point. Return "None"

print("In this list: {} Fixed point is: {}\n".format(A1 , find_fix_point(A1)))
print("In this list: {} Fixed point is: {}\n".format(A2 , find_fix_point(A2)))  
print("In this list: {} Fixed point is: {}\n".format(A3 , find_fix_point(A3)))   


# A bitonic sequence is a sequence of integers such that: x_0 < ... < x_k > ... > x_{n-1}
# 1, 2, 3, 4, 5, 4, 3, 2, 1 -> 5
def bitonic_peak(A):
    # my apporach is using binary search principle 
    
    if len(A)<3: # for bitonic sort at least we need 3 elements
        return None
    
    lower = 0 
    upper = len(A) - 1
    
    
    while lower <=upper:
        mid = (lower + upper) // 2
        
        left = A[mid - 1] if mid - 1 >= 0 else float('-inf')
        right= A[mid + 1] if mid + 1 < len(A) else float('inf')
        
        if A[mid] > left and A[mid] < right:
            lower = mid + 1
        elif A[mid] <left and A[mid] > right:
            upper = mid - 1 
        elif A[mid] > left and A[mid] > right:
            return A[mid]  
    return None

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print("for this bitonic sorted array: {} peak is: {}".format(A, bitonic_peak(A)))
A = [1, 6, 5, 4, 3, 2, 1]
print("for this bitonic sorted array: {} peak is: {}".format(A, bitonic_peak(A)))
A = [1, 2, 3, 4, 5]
print("for this bitonic sorted array: {} peak is: {}".format(A, bitonic_peak(A)))
A = [5, 4, 3, 2, 1]
print("for this bitonic sorted array: {} peak is: {}\n".format(A, bitonic_peak(A)))

def first_occurance(A,target)->int or None: #find the first occurance of dublicate number
    # Array is sorted Asending
    if len(A) == 0:
        return None
    
    lower = 0
    upper = len(A) - 1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if A[mid] < target:
            lower = mid + 1
        elif A[mid]>target:
            upper = mid - 1
        else:
            if mid - 1 <0:
                return mid
            if A[mid - 1] != target:
                return mid
            upper = mid - 1
    return None
A = [-14, -11 ,-10, 2, 108, 108, 243, 401,401,401]

print("In the following list {} 108 first apperance is at index: {}".format(A, first_occurance(A,108)))

# You are required to write a function that takes a non-negative integer, k, and returns the largest integer
# whose square is less than or equal to the specified integer k.

# To solve this we can use binary search algo 
# 1st numbers are sorted by default from 1 to target
# we look for a largest x such that x^2 <= target
def nearest_squar_root( target)->int:
    if target <=0 :
        return None
    
    low = 1
    high = target // 2 # since we looking for a x that x^2 <= target
    
    while low<= high:
        mid = (low + high) //2
        
        if mid*mid < target:
            sq = mid   # sq would have the largest x
            low = mid + 1
        elif mid*mid > target:
            high = mid - 1 
        else:
            return mid
    return sq

print("\nnearset number's squar root to the number 300 is {} \n".format(nearest_squar_root(300)))

# Exercise: Cyclically Shifted Array
# Challenge yourself with an exercise in which you'll have to return the index of the smallest number in a cyclically shifted array.

def find(A):

  low = 0 
  high = len(A) - 1
  while low <= high:
    mid = (low + high) // 2
    if A[mid] < A[high]:
      high = mid
    else:
      low = mid +1 
  return low - 1

# print(find([5, 6, 7, 1, 2, 3, 5]))
find([1, 2, 3, 4, 5, 6, 7])


# from bisect import bisect, bisect_left, bisect_right

# from binarySearch import binary_search


# A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]


# print(bisect_left(A,108))

# print(bisect_right(A,108))

# print(bisect(A,108))

# binary_search()