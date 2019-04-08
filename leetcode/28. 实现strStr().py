class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        index = -1
        first = needle[0]
        haystack_len = len(haystack)
        for i in range(haystack_len):
            if haystack[i] == first and haystack_len >= needle_len + i:
                t = index = i
                for j in range(1, needle_len):
                    t += 1
                    if needle[j] != haystack[t]:
                        index = -1
                if index != -1:
                    break
        return index


if __name__ == "__main__":
    haystack = "aaaaal"
    needle = "al"
    print(Solution().strStr(haystack, needle))
