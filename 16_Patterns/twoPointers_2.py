# Problem 1) Triplet sum to zero (medium)
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

def search_triplets(arr):
  # check there is atleast three elements
  if(len(arr) < 3):
    return 0
  triplets = []
  arr.sort()
  primaryPointer = 0

  while primaryPointer < len(arr):
    targetNum = arr[primaryPointer]
    temp = match(arr[primaryPointer+1::], (targetNum *-1))

    if temp:
        for lst in temp:
          lst.insert(0,arr[primaryPointer])
          triplets.append(lst)
    primaryPointer +=1

  return triplets

def match(arr:list, targetNum: int)->list: 
  if(len(arr) < 3):
    return None
  
  valueIndexMap = dict()
  result = []
  xPointer = 0
  yPointer = len(arr) - 1

  while xPointer < yPointer:
    if arr[xPointer] + arr[yPointer] < targetNum:
      xPointer += 1      
    elif arr[xPointer] + arr[yPointer] > targetNum:
      yPointer -= 1
    else:
      temp = list()
      temp.append(arr[xPointer])
      temp.append(arr[yPointer])
      result.append(temp)

      xPointer += 1
      yPointer -= 1
  return result


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))


# problem 2
# Given an array of integers, nums, and an integer value, target,
# determine if there are any three integers in nums whose sum equals the target.
# Return TRUE if three such integers are found in the array. Otherwise, return FALSE.
def find_sum_of_three(nums, target):

   if len(nums) <3:
      return False
   k = target

   # a+b+c = k => c = k-a-b => k - c  = a + b

   nums_sorted_acending = sorted(nums)

   indexes_three_digits = list()
   for i in range(len(nums_sorted_acending)):

      index_of_a_and_b = find_a_b(nums_sorted_acending[i+1::],k - nums_sorted_acending[i] )

      if index_of_a_and_b:
         index_of_a_and_b.append(i)
         indexes_three_digits.append(index_of_a_and_b)
         print(indexes_three_digits)
   if indexes_three_digits:
      return True
   return False


def find_a_b(nums:list, c:int)->list:
   x_pointer = 0
   y_pointer =  len(nums) - 1 
   a_b_indexes = list()
   print(nums, " ", c)
   while x_pointer < y_pointer:

      if nums[x_pointer] + nums[y_pointer] > c:
         y_pointer -=1
      elif nums[x_pointer] + nums[y_pointer] < c:
         x_pointer +=1
      else:
         a_b_indexes.append(x_pointer)
         a_b_indexes.append(y_pointer)
         break
   return a_b_indexes
 
# problem 2 another way
def find_sum_of_three(nums, target):
    # Sorting the input list
    nums.sort()

    # Fix one element at a time and find the other two
    for i in range(0, len(nums)-2):
        # Set the indexes of the two pointers

        # Index of the first of the remaining elements
        low = i + 1

        # Last index
        high = len(nums) - 1

        while low < high:
            # Check if the sum of the triple is equal to the sum
            triple = nums[i] + nums[low] + nums[high]
            # Found a triple whose sum equals the target
            if triple == target:
                return True
                # Move low pointer forward if the triple sum is less
                # than the required sum
            elif triple < target:
                low += 1
                # Move the high pointer backwards if the triple
                # sum is greater than the required sum
            else:
                high -= 1
    return False
# problem 3
# Write a function that takes a string as input and checks whether
# it can be a valid palindrome by removing at most one character from it.

def is_palindrome(s):
  x_pointer = 0
  y_pointer = len(s) - 1
  ignore_char = True
  while x_pointer < y_pointer:
    if s[x_pointer] == s[y_pointer]:
      x_pointer+=1 
      y_pointer-=1
    else:
      if s[x_pointer+1] == s[y_pointer] and ignore_char:
        x_pointer +=1
        y_pointer -=2
        ignore_char = False
      elif s[x_pointer] == s[y_pointer-1] and ignore_char:
        x_pointer+=1
        y_pointer-=2
        ignore_char = False
      else:
        return False
  return True  

print(is_palindrome("eeccccbebaeeabebccceea"))