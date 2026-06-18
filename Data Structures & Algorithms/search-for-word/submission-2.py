class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, cur):
            # bounds + visited check
            if (
                r < 0 or r >= Rows or
                c < 0 or c >= Cols or
                (r, c) in visited
            ):
                return False

            # add current character
            cur += board[r][c]

            # prune early (very important)
            if not word.startswith(cur):
                return False

            # found full word
            if cur == word:
                return True

            visited.add((r, c))

            found = (
                dfs(r + 1, c, cur) or
                dfs(r - 1, c, cur) or
                dfs(r, c + 1, cur) or
                dfs(r, c - 1, cur)
            )

            visited.remove((r, c))

            return found

        # try starting DFS from every cell
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r, c, ""):
                    return True

        return False