class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        ret = 0
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ret += 1
        return ret


if __name__ == "__main__":
    people = [1, 2, 3]
    limit = 3
    print(Solution().numRescueBoats(people, limit))
