def find_highest_number(A):
    #bitnic order [1,2,...5,4,3..1] highest is 5
    # array is sorted in bitonic 
    size = len(A)
    if size < 3:
        return None
    
    lower_bound = 0
    upper_bound = size-1
    

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
    
        
        mid_left = A[mid - 1] if mid - 1 >= 0 else float('-inf')
        mid_right = A[mid + 1] if mid + 1 <  size else float('inf')
        
        
        if mid_left < A[mid] and mid_right > A[mid]:
            lower_bound = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            upper_bound = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]

        # if mid_left < A[mid] and mid_right > A[mid]:
        #     lower_bound = mid + 1
    
        # elif mid_right > A[mid] and mid_left < A[mid]:
        #     upper_bound = mid - 1
            
        # elif A[mid] > mid_left and A[mid] > mid_right:
        #     return A[mid]
        
    return None 

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))