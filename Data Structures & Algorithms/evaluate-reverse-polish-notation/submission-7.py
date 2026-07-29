class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if len(t) > 1 or t.isdigit():
                stack.append(int(t))
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                b = stack.pop()
                stack.append(stack.pop() - b)
            else:  # "/"
                b = stack.pop()
                stack.append(int(stack.pop() / b))

        return stack[0]