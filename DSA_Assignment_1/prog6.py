#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def postfix_to_prefix(postfix):
    stack = []

    for token in postfix.split():
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = f"{token} {operand1} {operand2}"
            stack.append(expression)

    return stack.pop()


postfix = "3 4 5 * +"
prefix = postfix_to_prefix(postfix)
print(prefix)  # '+ 3 * 4 5'