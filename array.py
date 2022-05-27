# 1) Array Advance Game
# 2) Arbitrary Precision Increment
# 3) Two Sum Problem
# 4) Optimal Task Assignment
# 5) Intersection of Two Sorted Arrays
# 6) buy and sell stock 



# 1) Array Advance Game

# [3,3,1,0,2,0,1]
# Each number in the array represents the maximum you can advance in the array. 
# Is it possible to advance from the start of the array to the last element given that the maximum you can
# advance from a position is based on the value of the array at the index you are currently present on?

# [3,3,1,0,2,0,1] =>  Moves : 1,3,2 win
# [1,3,1,0,2,0,1] =>  

# greedy approach 
 # greedy approach in which we always advance the maximum we can at every index
 # is not solvable using greedy approch # [3,3,1,0,2,0,1] =>  Moves : 1,3,2 win this is a win last index is reachable but not with greedy algo
 
# None- greedy Algorithm
# We have to figure out the best way to advance in the array so that we reach the last index.

# i = 0 
# fourthest_reach = 0
# fourthest_reach = max(fourthest_reach, A[i] + i)
# If for some i, we don’t reach the end and that is the furthest we can reach, then we can’t reach the last index. Otherwise, the end is reached.
from typing import Dict


def array_advance(A):
    fourthest_reach = 0
    index = 0
    last_index = len(A)-1
    while index <= fourthest_reach and fourthest_reach < last_index:
        fourthest_reach = max(fourthest_reach,A[index]+index)
        index +=1
        # if fourthest_reach is equal or greater than last_index that means Array is reachable
    return fourthest_reach >= last_index   


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A)) # True

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A)) # False

# True: posible to navigate to last index in A:
# Moves: 2,3
A = [4,1,3,0,0,1]
# print(array_advance(A)) # True

print()
print("1) Array Advance Game time complexity O(n)")
print("A = {} , and is last index approachable: {}".format(A , array_advance(A)))

# 2) Arbitrary Precision Increment

# Given: An array of non-negative digits that represent a decimal integer.
# Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.
# For an array A,
#     Add 1 to the rightmost digit.
#     Propagate carry throughout the array.

array_1 = [1, 4, 9]
array_2 = [9, 9, 9]

def plus_one_pythonic(A):
    res = ''.join(map(str , A))
    res = int(res)+1
    B = [int(x) for x in str(res)]
    return B


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
print()
print("2) Arbitrary Precision Increment time complexity O(n)")

print("array_1 = {}".format( array_2), end =" ")
res = plus_one(array_2)
print("after adding 1 is: {}".format(res))
print()

# 3) Two Sum Problem - We investigate three different approaches to solving this problem.

# Given an array of integers, return True or False if the array has two numbers that add up to a specific target.
# You may assume that each input would have exactly one solution.

array_a = [-2, 1, 2, 4, 7, 11]
target = 13
# 3.1 
# time complexity O(n^2)
# space complexity O(1)
def two_sum_brute_force(list_A,key):
    for i in list_A:
        a = i
        b = key - i
        if b in list_A:
            print(a,b)
            return True
    return False

# 3.2
# time complexity O(n)
# space complexity O(n)
def two_sum_hash_table(list_A , target):
    ht = dict()  # a + b = target
    for i in range(len(list_A)):
        if list_A[i] in ht:
            print(list_A[i] ,  ht[list_A[i]])
            print(ht.items())
            return True
        else:
            ht[target - list_A[i]] = list_A[i]
    print(ht.items())
    return False
#3.3
# time complexity O(n)
# space complexity O(1)

# for this solution to work array must be sorted.
# Here, we have two indices that we keep track of, one at the front and one at the back.
# We move either the left or right indices based on whether the sum of the elements
# at these indices is either greater than or less than the target element.

def two_sum( list_A , target):
    i = 0
    j = len(list_A) - 1
    
    while i < j :
        if list_A[i] + list_A[j] == target:
            print(list_A[i] , list_A[j])
            return True
        elif  list_A[i] + list_A[j] < target:
            i +=1
        else:
            j -=1
    return False

print()
print("3) Two sum of pairs Task. using two pointers approach time  complexity :O(n), space complexity O(1)")
print("A = {} and target is: {}".format(A , target) , end=" => ")
two_sum(array_a, target)
print()


# 4) Optimal Task Assignment

# Assign tasks to workers so that the time it takes to complete all the tasks is minimized 
# given a count of workers and an array where each element indicates the duration of a task.
# We wish to determine the optimal way in which to assign tasks to some workers.
# Each worker must work on exactly two tasks.
# Tasks are independent of each other, and each task takes a certain amount of time.

task_duration = [2,7,5,5,3,6]
workers = 3

def diveWork(array_t , workers):
    array_t.sort()  # sort the array
    size = len(array_t)
    if(size == 0):
        return -1
    for i in range(size//2): 
        print(array_t[i] , array_t[~i]) #~i is bitwise complement operator which puts a negative sign in front of i and subtracts 1 from it.
    print()
        
print("4) Optimal Task Assignment task hours are:{} , and number of workers is: {}".format(task_duration, workers))
diveWork(task_duration,workers)

# 5) Intersection of Two Sorted Arrays

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# there is one line pythonic solution if the two arrays are not sorted
print("one-line pythonic solution if the two arrays are not sorted")
print(set(A).intersection(B))

#since two arrays are sorted we can come-up with a better algo 

def find_intersection(array_1 , array_2):
    intersections = []
    i =0 
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] == array_2[j]:
            if array_1[i] != array_1[i-1]:
                intersections.append(array_1[i])
            i+=1
            j+=1
        elif array_1[i] < array_2[j]:
            i+=1
        else:
            j+=1
    return intersections

        
print("The intersection between A={} and B={} is:{}".format(A,B,find_intersection(A,B)))




# Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another.

# In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on that day.

# Here is the way to calculate the profit:

#     Profit = Selling Price - Buying Price

# time compelxity O(n)
def buy_and_sell_stock_once(prices):
    
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        
        min_price = min(min_price,price)
        compare_profit = price - min_price
        max_profit =max(max_profit, compare_profit)
        
    return max_profit

A= [110, 215, 180, 335, 5] #225

#buy_and_sell_stock_once([50, 40, 30, 20, 10]) => 0 profit
#buy_and_sell_stock_once([100, 180, 260, 310, 40, 535, 695]) => 655
#buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])=>30
print()
print("5) buy and sell stock, find the the maximum possible profit time complexity O(n)")
print("for the following days {} the max_profit is: {}".format(A,buy_and_sell_stock_once(A)))
print()