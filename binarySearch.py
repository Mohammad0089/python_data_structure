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
    mid = (low + high) // 2
    
    if data[mid] == target:
        return True
    elif data[mid] < target:
        return binary_search_recursive(data,target,mid+1,high)
    else:
        return binary_search_recursive(data,target,low,mid-1)    

data = [1,3,4,8,9,12,14,18,22,85]
res  =  binary_search_recursive(data , 12,0,len(data) - 1)
print(res)