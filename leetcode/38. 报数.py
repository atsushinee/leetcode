class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        pre = self.countAndSay(n - 1)
        pre_len = len(pre)
        ans = []
        i = 0
        while i < pre_len:
            pre_val = pre[i]
            j = i + 1
            while j < pre_len:
                if pre_val != pre[j]:
                    break
                j += 1
            ans.append(str(j - i))
            ans.append(str(pre_val))
            i = j
        return "".join(ans)


if __name__ == '__main__':
    for i in range(1, 8):
        print(Solution().countAndSay(i))
