class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs_len = len(strs)
        if strs_len == 0:
            return ""
        first_str = strs[0]
        first_str_len = len(first_str)

        for i in range(first_str_len):
            for j in range(1,strs_len):
                if i >= len(strs[j]) or first_str[i] != strs[j][i]:
                    return first_str[:i]
        return first_str


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
