#Q7. Write a program to convert prefix expression to infix expression.
def prefix_to_infix(prefix):
    stack = []

    for token in reversed(prefix.split()):
        if token.isdigit():
            stack.append(token)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = f"({operand1} {token} {operand2})"
            stack.append(expression)

    return stack.pop()


prefix = "+ * 4 5 3"
infix = prefix_to_infix(prefix)
print(infix) 
