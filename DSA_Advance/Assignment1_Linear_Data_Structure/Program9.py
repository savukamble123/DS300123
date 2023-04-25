#9:Evaluate a postfix expression using stack

def evaluate_postfix(expression):
   
    stack = []

   
    for char in expression:
       
        if char.isdigit():
            stack.append(int(char))

        elif char in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()

       
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()
expression = "62+5*8/2-"
result = evaluate_postfix(expression)
print(result) 