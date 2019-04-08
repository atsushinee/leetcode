class Solution:
    def isValid(self, s: str) -> bool:
        s_len = len(s)
        if s_len % 2 == 1:
            return False
        if s_len == 0:
            return True
        stack = []

        m = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        for c in s:
            if c in m.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != m[stack.pop()]:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    A = "()[]{}"
    B = "()"
    C = "(]"
    D = "([)]"
    E = "{[]}"
    F = "){"
    G = "(("
    print(Solution().isValid(A))
    print(Solution().isValid(B))
    print(Solution().isValid(C))
    print(Solution().isValid(D))
    print(Solution().isValid(E))
    print(Solution().isValid(F))
    print(Solution().isValid(G))
