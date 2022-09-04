# def make_squares(arr):
  
#   squares = [ 0 for x in range(len(arr))]
#   left, right = 0, len(arr) - 1
#   highestSquare = len(arr) - 1

#   while left <= right:
#     rightSquare = arr[right] * arr[right]
#     leftSquare = arr[left] * arr[left]
  
#     if rightSquare >= leftSquare:
#       squares[highestSquare] = rightSquare
#       highestSquare -=1
#       squares[highestSquare] = leftSquare
#       highestSquare -=1
#       right -=1
#       left +=1

#     else:
#       squares[highestSquare] = leftSquare
#       highestSquare -= 1
#       squares[highestSquare] = rightSquare
#       highestSquare -=1
#       right -=1
#       left +=1
#   return squares

def make_squares(arr):
  
  squares = [0 for x in range(len(arr))]
  left, right = 0, len(arr) - 1
  highestSquare = len(arr) -1

  while left <= right:
    rightSquare = arr[right] * arr[right]
    leftSquare = arr[left] * arr[left]
  
    if rightSquare >= leftSquare:
      squares[highestSquare] = rightSquare
      highestSquare -=1
      right -=1
     

    else:
      squares[highestSquare] = leftSquare
      highestSquare -= 1
      left +=1
      
  return squares
def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()