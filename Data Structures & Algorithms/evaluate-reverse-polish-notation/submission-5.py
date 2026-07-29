import operator
from functools import reduce


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        note_dict = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for tok in tokens:
            if tok not in note_dict:
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(note_dict[tok](a, b))

        return stack[0]
