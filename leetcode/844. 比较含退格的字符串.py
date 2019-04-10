"""

给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。



示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。


提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_len = len(S)
        T_len = len(T)
        S_stack = []
        T_stack = []
        for i in range(S_len):
            if S[i] != "#":
                S_stack.append(S[i])
            else:
                if len(S_stack) > 0:
                    S_stack.pop()

        for i in range(T_len):
            if T[i] != "#":
                T_stack.append(T[i])
            else:
                if len(T_stack) > 0:
                    T_stack.pop()
        return "".join(S_stack) == "".join(T_stack)


if __name__ == '__main__':
    pass
