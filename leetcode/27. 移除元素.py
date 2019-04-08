from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        ans = 0
        for i in range(nums_len):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1
        return ans


if __name__ == "__main__":
    nums = []
    val = 2
    print(Solution().removeElement(nums, val))
    print(nums)
