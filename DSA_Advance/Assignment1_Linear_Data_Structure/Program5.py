#5:Find duplicates in an array
def find_duplicates(arr):
    duplicates = set()
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

arr = [1, 2, 3, 3, 4, 4, 5]
print(find_duplicates(arr))