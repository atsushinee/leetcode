from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high-low) // 2
            item = nums[mid]
            if target == item:
                return mid
            if target < item:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    input1 = [1, 3, 5, 6]
    target1 = 0
    print(Solution().searchInsert(input1, target1))
