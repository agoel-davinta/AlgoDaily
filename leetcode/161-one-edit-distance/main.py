"""
    naive approach:
    1. check insertion
    2. check replacement
    3. check deletion

    Time    O(128S+128S+S)
    Space   O(1)
    TLE
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t:
            return False
        # alphabets = "abcdefghijklmnopqrstuvwxyz"
        # check insertion
        for i in range(len(s) + 1):
            for j in range(128):
                alphab = str(chr(j))
                temp = s[:i] + alphab + s[i:]
                if temp == t:
                    return True
        # check replacement
        for i in range(len(s)):
            for j in range(128):
                alphab = str(chr(j))
                temp = s[:i] + alphab + s[i+1:]
                if temp == t:
                    return True
        # check deletion
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == t:
                return True
        return False


a = "ab"
b = "acb"
print(Solution().isOneEditDistance(a, b))

a = "cab"
b = "ad"
print(Solution().isOneEditDistance(a, b))

a = "1203"
b = "1213"
print(Solution().isOneEditDistance(a, b))

print("------------------")

"""
    1st approach:
    1. check if the result of removing of any character in s equals t
    2. check if the result of removing of any character in t equals s
    3. check if removing any same-positioned character in both s and t which makes them the same

    Time    O(S+T+min(S,T))
    Space   O(1)
    124 ms, faster than 5.18%
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t:
            return False
        # check remove s
        for i in range(len(s)):
            x = s[:i] + s[i+1:]
            if x == t:
                return True
        # check remove t
        for i in range(len(t)):
            x = t[:i] + t[i+1:]
            if x == s:
                return True
        # since we now check 'edit', both strings must have length
        if len(s) != len(t):
            return False
        # check remove s and remove t
        for i in range(len(s)):
            x = s[:i] + s[i+1:]
            y = t[:i] + t[i+1:]
            if x == y:
                return True
        return False


a = "ab"
b = "acb"
print(Solution().isOneEditDistance(a, b))

a = "cab"
b = "ad"
print(Solution().isOneEditDistance(a, b))

a = "1203"
b = "1213"
print(Solution().isOneEditDistance(a, b))

print("------------------")

"""
    2nd approach: check substrings
	- when we encounter different characters at the same index, compare the remaining substrings

	There're 3 possibilities to satisfy the question:
	1) Replace 1 char:
 	  s: a X b c
 	  t: a Y b c
    2) Delete 1 char from s:
        s: a X  b c
        t: a    b c
    3) Delete 1 char from t
        s: a   b c
        t: a X b c

	Time		O(min(S,T))
	Space		O(1)
    20 ms, faster than 97.86% 
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        minLen = min(len(s), len(t))
        for i in range(minLen):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) < len(t):
                    # remove one character from t
                    return s[i:] == t[i+1:]
                else:
                    # remove one character from s
                    return s[i+1:] == t[i:]
        # after we have done all the above
        # if the s is just one digit away from t, return true
        # e.g. "" and "a"
        if abs(len(s)-len(t)) == 1:
            return True
        return False


a = "ab"
b = "acb"
print(Solution().isOneEditDistance(a, b))

a = "cab"
b = "ad"
print(Solution().isOneEditDistance(a, b))

a = "1203"
b = "1213"
print(Solution().isOneEditDistance(a, b))
