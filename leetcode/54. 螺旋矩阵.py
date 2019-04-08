class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        ans = []
        if m == 0:
            return ans
        n = len(matrix[0])
        if n == 0:
            return ans
        size = m * n

        right, down, left, up = 1, 2, 3, 4
        max_right_step, max_down_step, max_left_step, max_up_step = n - 1, m - 1, 0, 0

        direction = right
        x, y = 0, 0
        while size > 0:
            if direction == right:
                while y <= max_right_step:
                    ans.append(matrix[x][y])
                    y += 1
                    size -= 1
                x += 1
                y -= 1
                direction = down
                max_up_step += 1
            elif direction == down:
                while x <= max_down_step:
                    ans.append(matrix[x][y])
                    x += 1
                    size -= 1
                x -= 1
                y -= 1
                direction = left
                max_right_step -= 1
            elif direction == left:
                while y >= max_left_step:
                    ans.append(matrix[x][y])
                    y -= 1
                    size -= 1
                y += 1
                x -= 1
                direction = up
                max_down_step -= 1
            elif direction == up:
                while x >= max_up_step:
                    ans.append(matrix[x][y])
                    x -= 1
                    size -= 1
                y += 1
                x += 1
                direction = right
                max_left_step += 1
        return ans


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(Solution().spiralOrder(matrix))
