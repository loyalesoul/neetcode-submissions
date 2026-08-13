class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        
        def dfs(index, current_path):
            # Base case 🎯
            if len(current_path) == len(digits):
                res.append("".join(current_path))
                return
                
            # Recursive step 🧭
            for letter in digit_to_char[digits[index]]:
                current_path.append(letter)      # 1. ADD
                dfs(index + 1, current_path)     # 2. EXPLORE
                current_path.pop()               # 3. UNDO
                
        dfs(0, [])
        return res