"""
    1st appraoch: bottom-up iterative

    dp[0] = 1
    dp[1] = 1
    dp[2] = 0 + 1 = 2
    dp[3] = 1 + 2 = 3
    dp[4] = 2 + 3 = 5
    dp[5] = 3 + 5 = 8
    dp[6] = 5 + 8 = 13

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	12ms beats 98.53%
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


print(Solution().climbStairs(0))
print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(13))
print(Solution().climbStairs(40))

print("-----")


"""
    2nd approach: top-down recursive
    - use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	n for hashtable, n for recursive callstack
	20 ms, faster than 66.37%
"""


class Solution(object):

    def __init__(self):
        self.cache = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            # when n == 0, we retuen 1 because it means this path be subtracted down to 0
            return 1
        elif n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]


print(Solution().climbStairs(0))
print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(13))
print(Solution().climbStairs(40))
