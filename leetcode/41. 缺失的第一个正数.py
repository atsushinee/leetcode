class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums_copy = set()
        ret = 1
        for n in nums:
            if n > 0:
                nums_copy.add(n)
        nums_copy = list(nums_copy)
        nums_copy.sort()
        if len(nums_copy) > 0 and nums_copy[0] < 2:
            temp_record = {nums_copy[0]: True}
            for i in range(1, len(nums_copy)):
                if temp_record.get(nums_copy[i] - 1, False):
                    temp_record[nums_copy[i]] = True
                else:
                    break
            l = list(temp_record.keys())
            l.sort()
            ret = l[-1] + 1
        return ret


if __name__ == "__main__":
    nums = [0, 2, 2, 1, 1]
    print(Solution().firstMissingPositive(nums))
