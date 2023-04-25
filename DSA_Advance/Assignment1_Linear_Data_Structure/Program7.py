#7:Move all the negative elements to one side of the array
def move_negatives(arr):
    n = len(arr)
    left, right = 0,n-1
    while left <= right:
     if arr[left] < 0 and arr[right] < 0:
      left += 1
     elif arr[left] >= 0 and arr[right] < 0:
       arr[left], arr[right] = arr[right], arr[left]
       left += 1
       right -= 1
     elif arr[left] >= 0 and arr[right] >= 0:
      right -= 1
     else:
       left += 1
       right -= 1
    return arr


arr = [2, -5, 7, -8, -6, 9, -1]
print(move_negatives(arr)) 