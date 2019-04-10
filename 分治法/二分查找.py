from typing import List


def binary_search(nums: List[int], target: int, low: int, high: int):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, high)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    target1 = 2
    print(binary_search(nums1, target1, 0, len(nums1) - 1))
