class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # Base Case 1: Matched all letters!
            if i == len(word):
                return True

            # Base Case 2: Out of bounds or character mismatch
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False

            # 1. ADD / MARK
            temp = board[r][c]
            board[r][c] = "#"  # Mark as visited

            # 2. EXPLORE (4 directions)
            found = (
                dfs(r + 1, c, i + 1)  # Down
                or dfs(r - 1, c, i + 1)  # Up
                or dfs(r, c + 1, i + 1)  # Right
                or dfs(r, c - 1, i + 1)  # Left
            )

            # 3. UNDO / BACKTRACK
            board[r][c] = temp  # Restore original character

            return found

        # Try starting the search from EVERY cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
