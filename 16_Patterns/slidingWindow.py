

# problem 1
# find all subarrays average and return as a list  
# Averages of subarrays of size K, so K be the number of elements of the sub arrays

def find_averages_of_subarrays(k,arr):
    avg_list=list()
    window_sum, window_start = 0.0 , 0 
    for window_end in range (len(arr)):
        window_sum = arr[window_end] + window_sum   # we do summation until we reach end of the window 
        
        if window_end >= k-1:                       # if statement True to determine end of the window
            avg_list.append(window_sum/k)           # now since we in the if block that means we reached end of the window
            window_sum -= arr[window_start]         # for remove the startPos from the window so next iteration we add next element to it
            window_start +=1                        # we increment start pos by 1 
              
    return avg_list
result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))


# problem 2
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

def max_sum_subarray(k,arr):
    if k <=0:       # checking if k is not positive
        return -1
    max = 0.0
    
    window_sum, window_start = 0.0 , 0
    for window_end in range(len(arr)):
        if arr[window_end] <=0:           # checking if there is a negetive element 
            return -1
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            max = window_sum if window_sum > max else max
            window_sum -= arr[window_start]
            window_start +=1         
    return max

# Time Complexity
# The time complexity of the above algorithm will be O(N)
# O(N)

# Space Complexity#
# The algorithm runs in constant space O(1)
# O(1)


arr , k = [2, 3, 4, 1, 5] , 2
print("Subarray with maximum sum is:" , end = " ")
print(max_sum_subarray(k,arr))


# problem 3
# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

def smallest_subarray_sum(S: int, arr:list):
    
  length_sum = 0
  min_length_subarray = float('inf')
  window_start = 0
  window_sum = 0.0
    
  for window_end in range (len(arr)):
    window_sum += arr[window_end]
    length_sum +=1
    if window_sum >= S:
        while window_sum >= S:   # shrink the window
            min_length_subarray = min(length_sum , min_length_subarray)
            length_sum -=1
            window_sum -= arr[window_start]
            window_start +=1
      
  return min_length_subarray 
# Time Complexity#
# The time complexity of the above algorithm will be O(N)
# O(N). The outer for loop runs for all elements, and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be O(N+N)
# O(N+N), which is asymptotically equivalent to O(N)

# Space Complexity#
# The algorithm runs in constant space O(1)

print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


# problem 4
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str_1:str, k:int)->int:
  
  longest_sub, window_start, window_sum = 0, 0, 0
  chr_occurancy = dict()
  
  for window_end in range(len(str_1)):
    window_sum +=1
    
    if str_1[window_end] not in chr_occurancy:
      chr_occurancy[str_1[window_end]] = 0       # initial to zero since next line will run in any case
    chr_occurancy[str_1[window_end]] +=1
    
    while len(chr_occurancy.keys()) > k:
      chr_occurancy[str_1[window_start]] -=1
      if chr_occurancy[str_1[window_start]] == 0:
        chr_occurancy.pop(str_1[window_start])
      window_start +=1
      window_sum -=1
    longest_sub = max(window_sum, longest_sub)  #This statement must be here after while loop

  return longest_sub
  
 # problem 5      
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.
def fruits_into_baskets(fruits:list)->int:
  # TODO: Write your code here
  letter_occurancy = dict()
  for fruit in fruits:
    if fruit not in letter_occurancy:
      letter_occurancy[fruit] = 0
    letter_occurancy[fruit] +=1
  #result = sorted(letter_occurancy.values(),reverse=True)
 

  return letter_occurancy


fruit=['A', 'B', 'C', 'A', 'C']

print(fruits_into_baskets(fruit))


 # problem 6
 # Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str1:str)->int:
  # find longest sub that has all distincet values
  windowStart = 0
  chrOccurancy = dict()
  maxSubStringLength = float('-inf')

  for windowEnd in range(len(str1)):
    
    if str1[windowEnd] not in chrOccurancy:
      chrOccurancy[str1[windowEnd]] = 0
    chrOccurancy[str1[windowEnd]] += 1

    if chrOccurancy[str1[windowEnd]] >=2:
      maxSubStringLength = max(maxSubStringLength, windowEnd - windowStart)
      windowStart = windowEnd
      chrOccurancy.clear()

  return maxSubStringLength

print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
