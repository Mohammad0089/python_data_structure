

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

# problem 7
# Find Maximum in Sliding Window

# Given an integer array and a window of size w, 
# find the current maximum value in the window as it slides through the entire array.


def find_max_sliding_window(nums, window_size):
    # your code will replace this placeholder return statement
    if len(nums) <1 or window_size <1:
        return None
    
    window_start = 0
    window_max = float('-inf')
    res = []
    temp = [] 

    for window_end in range(len(nums)):
        temp.append(nums[window_end])

        if window_end - window_start +1 >= window_size:
            res.append(max(temp))
            temp.pop(0)
            window_start +=1

    return res
  
  # Problem 8
  # Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, such that every
  # character of str2 appears in sub_str in the same order as it is present in str2.
  
def min_window(str1, str2):

    min_substring = ""
    length = float('inf')

    str1_size, str2_size = len(str1), len(str2)
    str1_ptr, str2_ptr = 0, 0

    while str1_ptr < str1_size:

        if str1[str1_ptr] == str2[str2_ptr]:
            str2_ptr +=1

            if str2_ptr == str2_size:
                # that means that all the chars of str2 are in str1 so far.
                start, end = str1_ptr, str1_ptr + 1

                # now we will loop backward to get in the begign pos
                str2_ptr -=1 # decrement str2_ptr by 1 to put it in the last pos
                while str2_ptr >=0:
                    if str1[start] == str2[str2_ptr]:
                        str2_ptr -=1
                    start -=1
                start +=1 # to bring it back to the correct begining pos
                str2_ptr = 0 # to bring it back to the correct begining pos
                if end - start < length:
                    min_substring = str1[start:end:1]
                    length = end - start
                    
        str1_ptr +=1

    return min_substring
  
  
  # Problem 9
  # Repeated DNA Sequences
# this is a navie apporach where O(k*n^2) where k is the dna found in 
# the series and checked against the rest of the string. spcae coplexity is k*n

# The naive approach would be finding the first sequence of the required length and
# then checking the remaining string for any repetitions of the same sequence. This will cost O(k * n)
# O(k×n), where nn is the length of the string and kk is the required length of the repeated sequences.
# Next, we need to locate a different sequence of the required length and repeat the checking process.
# The overall complexity would thus be O(n \times k \times n)
# O(n×k×n), that is, O(k * n^2) O(k×n^2 )

# def find_repeated_sequences(s, k):
#     dna_repeated = dict()
#     window_start, window_end = 0, 0
#     size_s = len(s)
#     dna=""

#     while window_end <= size_s:
#         if window_end >= k:
#             dna = s[window_start:window_end:1]
#             if dna not in dna_repeated:
#                 dna_repeated[dna] = 1
#                 start_pos, end_pos = window_end, window_end + 1
#                 while end_pos <= size_s:
#                     if end_pos - start_pos >= k:
#                         dna_exam = s[start_pos:end_pos:1]
#                         start_pos +=1
#                         if dna == dna_exam:
#                             dna_repeated[dna] += 1    
#                     end_pos +=1 
#                 window_start +=1        
#         window_end +=1

#     res = [k for k, v in dna_repeated.items() if v > 1]

#     return set(res)
 
 #O(n) O(s[i]) 
 
def find_repeated_sequences(s, k):
    mapping = {'A':1, 'C':2,'G':3, 'T':4}
    a = len(mapping)
    window_start,window_end,window_hash = 0,0,0
    pattern=""
    matched_patterns, sequence_hashes = set(),set()
    for i in range(k):
        window_hash = window_hash + mapping[s[i]] * pow(a, k-(i+1))
        pattern = pattern+s[i]
    sequence_hashes.add(window_hash)
    while window_end < len(s):
        if window_end>=k:
            sequence_hashes.add(window_hash)
            window_hash = (window_hash - mapping[s[window_start]] * pow(a,k-1)) * a
            window_hash = window_hash + mapping[s[window_end]]
            window_start+=1
            pattern = s[window_start:window_end+1]
            if window_hash in sequence_hashes:  # important to do the checking at the very end 
                matched_patterns.add(pattern)
        window_end +=1
    return matched_patterns


print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC" , 8))


# probelm 9 Buy and sell stock

def max_profit(stock_prices):
    # your code will replace this placeholder return statement++
    if len(stock_prices)<2:
        return None
    window_start, window_end, window_sum = 0,1,0
    max_profit = float('-inf')
    while window_end < len(stock_prices):
        if stock_prices[window_end] < stock_prices[window_start]:
            window_start = window_end
        difference = stock_prices[window_end] - stock_prices[window_start]
        max_profit = max(max_profit, difference)
        if stock_prices[window_end] < stock_prices[window_start]:
            window_start = window_end

        window_end +=1

    return max_profit


print(max_profit([]))