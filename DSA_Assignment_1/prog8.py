#Q8. Write a program to check if all the brackets are closed in a given code snippet

def check_brackets(code):
    stack = []

    for char in code:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()

    return not stack


code = "def foo():\n    if a == b:\n        return (1 + 2) * 3\n    else:\n        return (4 + 5"
if check_brackets(code):
    print("All brackets are properly closed.")
else:
    print("There is an unclosed bracket in the code.")
