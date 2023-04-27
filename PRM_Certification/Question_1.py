n = int(input())
lst = []
for i in range(n):
    lst.append(input())

sorted_lst = sorted(lst, key=lambda x: x[-2])

print(sorted_lst)