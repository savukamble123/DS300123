def count_case(a):
    upper_count = 0
    lower_count = 0
    for i in a:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    print("No.of Upper case character : ",upper_count)
    print("No.of Lower case character : ",lower_count)

result = input("Enter the string : ")
count_case(result)