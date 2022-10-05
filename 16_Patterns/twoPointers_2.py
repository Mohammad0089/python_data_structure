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
    temp = match(arr[primaryPointer+1::], (targetNum * -1))

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