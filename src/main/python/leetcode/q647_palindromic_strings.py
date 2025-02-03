"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""

class Solution(object):

    def is_palindrome(self, st):
        size = len(st)
        for i in range(0, size / 2):
            if st[i] != st[size - i - 1]:
                return False
        return True

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_palindromes = 0
        str_len = len(s)
        i = 0
        while i < str_len:

            if i % 1 == 0:
                l = r = int(i)
            else:
                l = int(i - 0.5)
                r = int(i + 0.5)

            while l >= 0 and r < str_len:

                if s[l] == s[r]:
                    count_palindromes = count_palindromes + 1
                    l = l - 1
                    r = r + 1
                else:
                    break
            i = i + 0.5
        return count_palindromes


if __name__ == "__main__":
    sol = Solution()
    assert(sol.countSubstrings("abc") == 3)
    assert(sol.countSubstrings("aaa") == 6)
