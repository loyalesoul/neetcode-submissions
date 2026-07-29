import operator
from functools import reduce


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        note_dict = {
            "+": operator.add,
            "-": operator.sub,
            "/": lambda a, b: int(a / b),
            "*": operator.mul,
        }
        if len(tokens) == 1 and tokens[0] not in note_dict:
            return int(tokens[0])
        stack = []
        res = 0
        for tok in tokens:
            if tok not in note_dict:
                stack.append(int(tok))
            else:
                res = reduce(note_dict[tok], stack[-2:])
                del stack[-2:]
                stack.append(res)

        return res
