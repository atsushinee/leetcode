class Solution:
    def numRookCaptures(self, board) -> int:
        N = len(board)
        rx, ry = 0, 0
        sum = 0
        for x in range(N):
            for y in range(N):
                if board[x][y] == 'R':
                    rx = x
                    ry = y
        temp = []
        for x in range(rx):
            val = board[x][ry]
            self.check_to_append(temp, val)
        sum += self.check_end(temp)
        temp.clear()
        for x in range(rx, N):
            val = board[x][ry]
            self.check_to_append(temp, val)
        sum += self.check_start(temp)
        temp.clear()
        for y in range(ry):
            val = board[rx][y]
            self.check_to_append(temp, val)

        sum += self.check_end(temp)
        temp.clear()
        for y in range(ry, N):
            val = board[rx][y]
            self.check_to_append(temp, val)

        sum += self.check_start(temp)
        return sum

    def check_end(self, l):
        if(len(l) > 0 and l[-1] == 'p'):
            return 1
        return 0

    def check_start(self, l):
        if len(l) > 0 and l[0] == 'p':
            return 1
        return 0

    def check_to_append(self, l, val):
        if val == 'B' or val == 'p':
            l.append(val)


if __name__ == "__main__":
    b = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."], [
        ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    print(Solution().numRookCaptures(b))
