#4:In an array, Count Pairs with given sum
def count_pairs_with_sum(arr, target_sum):
    count = 0
    hash_table = {}
    for num in arr:
        if target_sum - num in hash_table:
            count += hash_table[target_sum - num]
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1
    return count
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
print(count_pairs_with_sum(arr, target_sum)) 