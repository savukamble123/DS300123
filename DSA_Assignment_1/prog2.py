#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [10, 2, 9, 7, 5]
reverse_array(arr)
print(arr)