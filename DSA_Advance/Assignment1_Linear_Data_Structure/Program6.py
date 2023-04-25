#6:Find the Kth largest and Kth smallest number in an array
def kth_largest_smallest(arr, k):
    n = len(arr)
    if k > n:
        return None
    arr.sort()
    return arr[k-1], arr[n-k]
arr = [3, 5, 1, 8, 9, 1]
k = 3
print(kth_largest_smallest(arr, k))  