pos = -1
def search(list , n):
    l = 0 
    u = len(list)
    while l <=u :
        mid = (l+u)//2
        if list[mid] == n :
            globals() ['pos'] = mid
            return pos
        else:
            if list[mid] < n:
                l =mid
            else : 
                u = mid
    return False
list1 = [7,2,6,3,8,9]
a = sorted(list1)
print(a)
n = 9

if search( a , n):
    print("fount " ,pos)
else:
    print("not found")