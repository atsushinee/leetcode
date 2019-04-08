class Solution:
    def majorityElement(self, nums):
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]

        m1, c1 = nums[0], 1
        m2, c2 = 0, 0

        for i in range(1, len(nums)):
            v = nums[i]
            if v == m1:
                c1 += 1
            elif v == m2:
                c2 += 1
            elif c1 == 0:
                m1 = v
                c1 = 1
            elif c2 == 0:
                m2 = v
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for n in nums:
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
        ret = []
        if c1 > len(nums) / 3:
            ret.append(m1)
        if c2 > len(nums) / 3:
            ret.append(m2)
        return ret


if __name__ == "__main__":
    l = [1, 2]
    print(Solution().majorityElement(l))
