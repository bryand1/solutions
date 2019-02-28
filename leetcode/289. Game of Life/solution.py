class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        flips = []
        rows = len(board)
        if rows:
            cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if self.flip(board[r][c], self.live_neighbors(board, r, c, rows, cols)):
                    flips.append((r, c))
        for r, c in flips:
            board[r][c] ^= 1

    def flip(self, live, live_neighbors):
        if live and live_neighbors < 2:
            return True
        elif live and (live_neighbors == 2 or live_neighbors == 3):
            return False
        elif live and live_neighbors > 3:
            return True
        elif not live and live_neighbors == 3:
            return True
        else:
            return False

    def live_neighbors(self, board, r, c, rows, cols):
        s = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if r + dr < 0 or r + dr == rows:
                    continue
                if c + dc < 0 or c + dc == cols:
                    continue
                s += board[r + dr][c + dc]
        return s
