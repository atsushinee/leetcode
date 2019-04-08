class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        L = len(position)
        m = {}
        for i in range(L):
            m[position[i]] = speed[i]
        position.sort(reverse=True)
        i = 1
        pre_spend = (target-position[0]) / m[position[0]]
        ans = 1
        while i < L:
            print(i)
            now_spend = (target-position[i])/m[position[i]]
            if(now_spend > pre_spend):
                pre_spend = now_spend
                ans += 1
            i += 1
        return ans


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(Solution().carFleet(target, position, speed))
