class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2+el1)
            elif tokens[i] == "-":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2-el1)
            elif tokens[i] == "/":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(int(el2/el1))
            elif tokens[i] == "*":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2*el1)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

