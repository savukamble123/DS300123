#8:Reverse a string using a stack data structure


def reverse_string(string):
    stack = []
    reversed_string = ""
    for char in string:
        stack.append(char)
    while len(stack) > 0:
        reversed_string += stack.pop()
    return reversed_string
my_string = "hello edyoda"
reverse_string = reverse_string(my_string)
print(reverse_string)