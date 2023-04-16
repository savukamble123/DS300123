#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target):
    pairs = []
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs


arr = [1, 2, 3, 4, 5, 6]
target = 9
pairs = find_pairs(arr, target)
print(pairs)
