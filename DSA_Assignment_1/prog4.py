#Q4. Write a program to print the first non-repeated character from a string?
def first_non_repeated_char(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None


s = "Hello World"
print(first_non_repeated_char(s)) 