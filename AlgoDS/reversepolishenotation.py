"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer

    def evalRPN(self, tokens):
        operators = ['+','-','*','/']
        
        numbers = []
        
        for token in tokens:
            if token not in operators:
                numbers.append(token)
            else:
                number1 = float(numbers.pop())
                number2 = float(numbers.pop())
                if token == '+':
                    result = number2 + number1
                elif token == '-':
                    result = number2 - number1
                elif token == '*':
                    result = number2 * number1
                    
                elif token =='/':
                    result = number2 / number1
                else:
                    pass
                
                result = int(result)
                result = str(result)
                
                numbers.append(result)
        
        fi = numbers[0]   
        fi = int(fi)
        return fi