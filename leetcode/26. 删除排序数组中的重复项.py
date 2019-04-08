from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        pre = nums[0]
        n = 1
        for i in range(1, nums_len):
            if nums[i] != pre:
                pre = nums[n] = nums[i]
                n += 1
        return n


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
    print(nums)
