class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}
        N = len(s)
        ans = 0
        for i in range(N):
            v = m.get(s[i])
            if i == N - 1 or m.get(s[i + 1]) <= v:
                ans += v
            else:
                ans -= v
        return ans


if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
