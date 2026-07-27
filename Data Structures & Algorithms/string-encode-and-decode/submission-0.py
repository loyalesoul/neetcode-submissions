from itertools import islice, takewhile

class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        it = iter(s)

        while length_digits := "".join(takewhile(lambda c: c != "#", it)):
            length = int(length_digits)
            res.append("".join(islice(it, length)))

        return res
